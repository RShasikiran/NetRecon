"""
cve_lookup.py — NVD CVE lookup module
Maps detected service versions to real CVEs with CVSS scores
"""

import urllib.request
import urllib.parse
import json
import time
import re


NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"

SEVERITY_MAP = {
    "CRITICAL": "#e74c3c",
    "HIGH":     "#e67e22",
    "MEDIUM":   "#f1c40f",
    "LOW":      "#2ecc71",
    "NONE":     "#95a5a6",
}


def cvss_to_severity(score):
    if score is None:
        return "UNKNOWN"
    score = float(score)
    if score >= 9.0: return "CRITICAL"
    if score >= 7.0: return "HIGH"
    if score >= 4.0: return "MEDIUM"
    if score >= 0.1: return "LOW"
    return "NONE"


class CVELookup:
    def lookup_from_nmap(self, nmap_data):
        """Build a dict: 'product version' -> list of CVEs"""
        cves = {}
        seen = set()

        for host in nmap_data.get("hosts", []):
            for port in host.get("ports", []):
                product = port.get("product", "").strip()
                version = port.get("version", "").strip()

                if not product:
                    continue

                key = f"{product} {version}".strip()
                if key in seen or key == "":
                    continue
                seen.add(key)

                cve_list = self._query_nvd(product, version)
                if cve_list:
                    cves[key] = cve_list

                time.sleep(0.6)  # NVD rate limit

        return cves

    def _query_nvd(self, product, version):
        keyword = f"{product} {version}".strip()
        params = urllib.parse.urlencode({
            "keywordSearch": keyword,
            "resultsPerPage": 5,
        })
        url = f"{NVD_API}?{params}"

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NetRecon/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
        except Exception:
            return []

        results = []
        for item in data.get("vulnerabilities", []):
            cve = item.get("cve", {})
            cve_id = cve.get("id", "N/A")

            descriptions = cve.get("descriptions", [])
            desc = next((d["value"] for d in descriptions if d.get("lang") == "en"), "No description available")
            desc = desc[:200] + "..." if len(desc) > 200 else desc

            # CVSS score
            metrics = cve.get("metrics", {})
            score = None
            for key in ["cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
                if key in metrics and metrics[key]:
                    score = metrics[key][0].get("cvssData", {}).get("baseScore")
                    break

            severity = cvss_to_severity(score)

            results.append({
                "id": cve_id,
                "description": desc,
                "cvss_score": score,
                "severity": severity,
                "severity_color": SEVERITY_MAP.get(severity, "#95a5a6"),
                "url": f"https://nvd.nist.gov/vuln/detail/{cve_id}",
            })

        return results
