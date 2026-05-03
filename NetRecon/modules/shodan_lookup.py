"""
shodan_lookup.py — Shodan passive enrichment module
Queries Shodan API for indexed data about a target IP
"""

import urllib.request
import urllib.parse
import json


class ShodanLookup:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base = "https://api.shodan.io"

    def lookup(self, target):
        # Resolve to IP if domain
        import socket
        try:
            ip = socket.gethostbyname(target)
        except Exception:
            ip = target

        url = f"{self.base}/shodan/host/{ip}?key={self.api_key}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NetRecon/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
        except Exception as e:
            return {"error": str(e), "ip": ip}

        ports = data.get("ports", [])
        vulns = list(data.get("vulns", {}).keys()) if data.get("vulns") else []
        hostnames = data.get("hostnames", [])
        tags = data.get("tags", [])

        return {
            "ip": ip,
            "org": data.get("org", "N/A"),
            "isp": data.get("isp", "N/A"),
            "country": data.get("country_name", "N/A"),
            "city": data.get("city", "N/A"),
            "latitude": data.get("latitude", 0),
            "longitude": data.get("longitude", 0),
            "ports": ports,
            "hostnames": hostnames,
            "os": data.get("os", "Unknown"),
            "tags": tags,
            "vulns": vulns,
            "last_update": data.get("last_update", "N/A"),
            "asn": data.get("asn", "N/A"),
        }
