"""
whois_dns.py — WHOIS and DNS enrichment module
Gathers domain ownership, registrar info, and DNS records
"""

import socket
import subprocess
import re


class WhoisDNS:
    def lookup(self, target):
        result = {
            "whois": self._whois(target),
            "dns": self._dns(target),
            "reverse_dns": self._reverse_dns(target),
        }
        return result

    def _whois(self, target):
        try:
            proc = subprocess.run(["whois", target], capture_output=True, text=True, timeout=15)
            raw = proc.stdout

            def extract(patterns, text):
                for p in patterns:
                    m = re.search(p, text, re.IGNORECASE | re.MULTILINE)
                    if m:
                        return m.group(1).strip()
                return "N/A"

            return {
                "registrant": extract([r"Registrant.*?:\s*(.+)", r"org:\s*(.+)", r"OrgName:\s*(.+)"], raw),
                "registrar": extract([r"Registrar:\s*(.+)", r"registrar:\s*(.+)"], raw),
                "created": extract([r"Creation Date:\s*(.+)", r"created:\s*(.+)", r"RegDate:\s*(.+)"], raw),
                "updated": extract([r"Updated Date:\s*(.+)", r"last-modified:\s*(.+)"], raw),
                "expires": extract([r"Registry Expiry Date:\s*(.+)", r"Expiry Date:\s*(.+)"], raw),
                "country": extract([r"Registrant Country:\s*(.+)", r"country:\s*(.+)", r"Country:\s*(.+)"], raw),
                "name_servers": re.findall(r"Name Server:\s*(.+)", raw, re.IGNORECASE),
                "status": extract([r"Domain Status:\s*(.+)", r"Status:\s*(.+)"], raw),
                "raw_snippet": raw[:800] if raw else "No WHOIS data available",
            }
        except Exception as e:
            return {"error": str(e), "registrant": "N/A", "registrar": "N/A"}

    def _dns(self, target):
        records = {}
        # Only run DNS lookups for domain-like targets
        is_domain = not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", target)

        if not is_domain:
            return {"note": "Target is an IP address, DNS records skipped"}

        record_types = ["A", "AAAA", "MX", "NS", "TXT", "SOA"]
        for rtype in record_types:
            try:
                proc = subprocess.run(
                    ["dig", "+short", rtype, target],
                    capture_output=True, text=True, timeout=10
                )
                lines = [l.strip() for l in proc.stdout.strip().split("\n") if l.strip()]
                records[rtype] = lines if lines else []
            except Exception:
                records[rtype] = []

        # Check for SPF, DMARC, DKIM
        spf = any("v=spf1" in r for r in records.get("TXT", []))
        dmarc_proc = subprocess.run(
            ["dig", "+short", "TXT", f"_dmarc.{target}"],
            capture_output=True, text=True, timeout=10
        )
        dmarc = bool(dmarc_proc.stdout.strip())

        records["security"] = {
            "spf": "Present" if spf else "Missing",
            "dmarc": "Present" if dmarc else "Missing",
            "spf_risk": "OK" if spf else "HIGH — phishing risk",
            "dmarc_risk": "OK" if dmarc else "HIGH — email spoofing risk",
        }

        return records

    def _reverse_dns(self, target):
        try:
            hostname = socket.gethostbyaddr(target)
            return {"hostname": hostname[0], "aliases": hostname[1]}
        except Exception:
            return {"hostname": "No PTR record", "aliases": []}
