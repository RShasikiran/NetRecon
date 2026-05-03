"""
scanner.py — Nmap scanning engine
Runs nmap with appropriate flags and parses XML output
"""

import subprocess
import xml.etree.ElementTree as ET
import os
import tempfile


INTENSITY_FLAGS = {
    "quick":      ["-sV", "-T4", "--open", "-F"],
    "normal":     ["-sV", "-sC", "-O", "-A", "--traceroute", "-T4"],
    "aggressive": ["-sV", "-sC", "-O", "-A", "--traceroute", "--script=vuln", "-T4", "-p-"],
}

DANGEROUS_PORTS = {
    21: ("FTP", "HIGH"),
    22: ("SSH", "MEDIUM"),
    23: ("Telnet", "CRITICAL"),
    25: ("SMTP", "MEDIUM"),
    53: ("DNS", "MEDIUM"),
    80: ("HTTP", "LOW"),
    110: ("POP3", "MEDIUM"),
    135: ("RPC", "HIGH"),
    139: ("NetBIOS", "HIGH"),
    443: ("HTTPS", "LOW"),
    445: ("SMB", "CRITICAL"),
    1433: ("MSSQL", "HIGH"),
    1521: ("Oracle DB", "HIGH"),
    3306: ("MySQL", "HIGH"),
    3389: ("RDP", "CRITICAL"),
    5432: ("PostgreSQL", "HIGH"),
    5900: ("VNC", "HIGH"),
    6379: ("Redis", "HIGH"),
    8080: ("HTTP-Alt", "LOW"),
    27017: ("MongoDB", "HIGH"),
}


class NmapScanner:
    def __init__(self, intensity="normal"):
        self.intensity = intensity
        self.flags = INTENSITY_FLAGS.get(intensity, INTENSITY_FLAGS["normal"])

    def scan(self, target):
        output_file = tempfile.mktemp(suffix=".xml")
        cmd = ["nmap"] + self.flags + ["-oX", output_file, target]

        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired:
            return {"error": "Nmap scan timed out", "hosts": [], "total_ports": 0}
        except FileNotFoundError:
            return {"error": "nmap not found. Please install nmap.", "hosts": [], "total_ports": 0}

        if not os.path.exists(output_file):
            return {"error": "Nmap did not produce output", "hosts": [], "total_ports": 0}

        result = self._parse_xml(output_file)
        os.remove(output_file)
        return result

    def _parse_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        hosts = []
        total_ports = 0

        for host in root.findall("host"):
            status = host.find("status")
            if status is None or status.get("state") != "up":
                continue

            host_data = {}

            # IP and hostname
            for addr in host.findall("address"):
                if addr.get("addrtype") == "ipv4":
                    host_data["ip"] = addr.get("addr")
                elif addr.get("addrtype") == "mac":
                    host_data["mac"] = addr.get("addr")
                    host_data["vendor"] = addr.get("vendor", "Unknown")

            hostnames = host.find("hostnames")
            if hostnames is not None:
                names = [h.get("name") for h in hostnames.findall("hostname") if h.get("name")]
                host_data["hostnames"] = names
            else:
                host_data["hostnames"] = []

            # OS Detection
            os_elem = host.find("os")
            if os_elem is not None:
                osmatch = os_elem.find("osmatch")
                if osmatch is not None:
                    host_data["os"] = osmatch.get("name", "Unknown")
                    host_data["os_accuracy"] = osmatch.get("accuracy", "0") + "%"
                else:
                    host_data["os"] = "Unknown"
                    host_data["os_accuracy"] = "0%"
            else:
                host_data["os"] = "Unknown"
                host_data["os_accuracy"] = "0%"

            # Ports
            ports = []
            ports_elem = host.find("ports")
            if ports_elem is not None:
                for port in ports_elem.findall("port"):
                    state_elem = port.find("state")
                    if state_elem is None or state_elem.get("state") != "open":
                        continue

                    port_num = int(port.get("portid"))
                    proto = port.get("protocol")

                    service_elem = port.find("service")
                    service_name = service_elem.get("name", "unknown") if service_elem is not None else "unknown"
                    product = service_elem.get("product", "") if service_elem is not None else ""
                    version = service_elem.get("version", "") if service_elem is not None else ""
                    extra_info = service_elem.get("extrainfo", "") if service_elem is not None else ""

                    scripts = {}
                    for script in port.findall("script"):
                        scripts[script.get("id")] = script.get("output")

                    danger_info = DANGEROUS_PORTS.get(port_num, (service_name, "INFO"))
                    port_risk = danger_info[1]

                    port_data = {
                        "port": port_num,
                        "protocol": proto,
                        "service": service_name,
                        "product": product,
                        "version": version,
                        "extra_info": extra_info,
                        "full_version": f"{product} {version} {extra_info}".strip(),
                        "scripts": scripts,
                        "risk": port_risk,
                    }
                    ports.append(port_data)
                    total_ports += 1

            host_data["ports"] = ports
            host_data["open_port_count"] = len(ports)

            # Traceroute
            trace_elem = host.find("trace")
            if trace_elem is not None:
                hops = []
                for hop in trace_elem.findall("hop"):
                    hops.append({
                        "ttl": hop.get("ttl"),
                        "ip": hop.get("ipaddr", "*"),
                        "rtt": hop.get("rtt", "N/A"),
                        "host": hop.get("host", "")
                    })
                host_data["traceroute"] = hops
            else:
                host_data["traceroute"] = []

            hosts.append(host_data)

        return {
            "hosts": hosts,
            "total_ports": total_ports,
            "scan_type": self.intensity,
            "flags_used": " ".join(self.flags),
        }
