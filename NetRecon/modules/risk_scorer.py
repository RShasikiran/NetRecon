"""
risk_scorer.py — Risk scoring engine
Assigns Critical/High/Medium/Low ratings to each host and overall target
"""


HIGH_RISK_PORTS = {
    23: 40,   # Telnet
    3389: 35, # RDP
    445: 35,  # SMB
    135: 25,  # RPC
    139: 25,  # NetBIOS
    21: 20,   # FTP
    5900: 25, # VNC
    1433: 25, # MSSQL
    3306: 20, # MySQL
    27017: 20,# MongoDB
    6379: 20, # Redis
    25: 15,   # SMTP
    110: 15,  # POP3
}

def score_to_label(score):
    if score >= 80: return ("CRITICAL", "#e74c3c")
    if score >= 55: return ("HIGH",     "#e67e22")
    if score >= 30: return ("MEDIUM",   "#f1c40f")
    return             ("LOW",      "#2ecc71")


class RiskScorer:
    def score(self, nmap_data, cves, shodan_data):
        host_scores = []

        for host in nmap_data.get("hosts", []):
            score = 0
            breakdown = []

            # Port-based scoring
            for port in host.get("ports", []):
                pnum = port["port"]
                if pnum in HIGH_RISK_PORTS:
                    pts = HIGH_RISK_PORTS[pnum]
                    score += pts
                    breakdown.append(f"Port {pnum} ({port['service']}) open +{pts}")

            # CVE scoring
            service_keys = [
                f"{p['product']} {p['version']}".strip()
                for p in host.get("ports", [])
                if p.get("product")
            ]
            for key in service_keys:
                for cve in cves.get(key, []):
                    cvss = cve.get("cvss_score")
                    if cvss:
                        pts = int(float(cvss) * 2)
                        score += pts
                        breakdown.append(f"{cve['id']} (CVSS {cvss}) +{pts}")

            # Shodan vuln tags
            if shodan_data and not shodan_data.get("error"):
                shodan_vulns = shodan_data.get("vulns", [])
                if shodan_vulns:
                    pts = len(shodan_vulns) * 10
                    score += pts
                    breakdown.append(f"Shodan-tagged {len(shodan_vulns)} vuln(s) +{pts}")

            score = min(score, 100)  # cap at 100
            label, color = score_to_label(score)

            host_scores.append({
                "ip": host.get("ip", "N/A"),
                "score": score,
                "label": label,
                "color": color,
                "breakdown": breakdown,
            })

        # Overall score = max host score
        if host_scores:
            top = max(host_scores, key=lambda x: x["score"])
            overall_score = top["score"]
        else:
            overall_score = 0

        overall_label, overall_color = score_to_label(overall_score)

        return {
            "hosts": host_scores,
            "overall_score": overall_score,
            "overall_label": overall_label,
            "overall_color": overall_color,
        }
