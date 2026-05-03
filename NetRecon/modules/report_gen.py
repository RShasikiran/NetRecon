"""
report_gen.py — HTML report generator
Produces a professional, Maltego-style visual report
"""

import os
import json
from datetime import datetime


class ReportGenerator:
    def generate_html(self, results, output_path):
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else "output", exist_ok=True)
        html_path = output_path + ".html"

        template = self._build_template(results)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(template)

        return html_path

    def generate_pdf(self, html_path):
        pdf_path = html_path.replace(".html", ".pdf")
        try:
            import subprocess
            subprocess.run(
                ["wkhtmltopdf", "--page-size", "A4", "--dpi", "300",
                 "--enable-local-file-access", html_path, pdf_path],
                capture_output=True, timeout=120
            )
        except Exception as e:
            print(f"  [!] PDF generation failed: {e}")
            return None
        return pdf_path

    def _build_executive_summary(self, results):
        target = results.get("target", "N/A")
        hosts = results.get("nmap", {}).get("hosts", [])
        risk = results.get("risk", {})
        cves = results.get("cves", {})
        total_cves = sum(len(v) for v in cves.values())
        critical_cves = sum(1 for vlist in cves.values() for v in vlist if v.get("severity") == "CRITICAL")
        total_ports = results.get("nmap", {}).get("total_ports", 0)
        overall = risk.get("overall_label", "UNKNOWN")
        subdomains = len(results.get("subdomains", []))

        lines = [f"Target <strong>{target}</strong> was scanned at {results.get('timestamp', 'N/A')}. "]
        lines.append(f"The scan discovered <strong>{len(hosts)} active host(s)</strong> with a total of <strong>{total_ports} open port(s)</strong>. ")

        if total_cves > 0:
            lines.append(f"CVE analysis identified <strong>{total_cves} vulnerabilities</strong>, of which <strong>{critical_cves} are rated CRITICAL</strong>. ")
        else:
            lines.append("No CVE matches were identified for the detected services. ")

        if subdomains > 0:
            lines.append(f"Subdomain enumeration discovered <strong>{subdomains} subdomain(s)</strong> expanding the attack surface. ")

        lines.append(f"Overall risk posture is rated <strong style='color:{risk.get('overall_color','#aaa')}'>{overall}</strong>. ")
        lines.append("Immediate remediation is recommended for all CRITICAL and HIGH findings listed below.")

        return "".join(lines)

    def _build_graph_nodes(self, results):
        nodes = []
        edges = []
        node_id = 1

        target = results.get("target", "target")
        nodes.append({"id": 0, "label": target, "group": "target", "title": f"Target: {target}", "size": 35})

        hosts = results.get("nmap", {}).get("hosts", [])
        for host in hosts:
            ip = host.get("ip", "N/A")
            host_id = node_id; node_id += 1
            risk_label = ""
            for h in results.get("risk", {}).get("hosts", []):
                if h["ip"] == ip:
                    risk_label = h["label"]
            nodes.append({"id": host_id, "label": ip, "group": "host", "title": f"Host: {ip} | OS: {host.get('os','?')} | Risk: {risk_label}", "size": 22})
            edges.append({"from": 0, "to": host_id})

            for port in host.get("ports", []):
                p_id = node_id; node_id += 1
                label = f"{port['port']}/{port['service']}"
                nodes.append({"id": p_id, "label": label, "group": port.get("risk", "INFO").lower(), "title": f"Port: {port['port']} | Service: {port['service']} | Version: {port.get('full_version','?')} | Risk: {port.get('risk','?')}", "size": 14})
                edges.append({"from": host_id, "to": p_id})

        for sub in results.get("subdomains", [])[:20]:
            s_id = node_id; node_id += 1
            nodes.append({"id": s_id, "label": sub["subdomain"], "group": "subdomain", "title": f"Subdomain: {sub['subdomain']} → {sub['ip']}", "size": 12})
            edges.append({"from": 0, "to": s_id})

        return json.dumps(nodes), json.dumps(edges)

    def _build_template(self, results):
        target = results.get("target", "N/A")
        timestamp = results.get("timestamp", "N/A")
        risk = results.get("risk", {})
        nmap = results.get("nmap", {})
        hosts = nmap.get("hosts", [])
        cves = results.get("cves", {})
        subdomains = results.get("subdomains", [])
        whois_dns = results.get("whois_dns", {})
        shodan = results.get("shodan") or {}
        diff = results.get("diff")
        exec_summary = self._build_executive_summary(results)
        graph_nodes, graph_edges = self._build_graph_nodes(results)
        total_cves = sum(len(v) for v in cves.values())
        critical_count = sum(1 for vl in cves.values() for v in vl if v.get("severity") == "CRITICAL")
        high_count = sum(1 for vl in cves.values() for v in vl if v.get("severity") == "HIGH")

        # Build port rows
        port_rows_html = ""
        for host in hosts:
            for port in host.get("ports", []):
                risk_colors = {"CRITICAL": "#e74c3c", "HIGH": "#e67e22", "MEDIUM": "#f1c40f", "LOW": "#2ecc71", "INFO": "#3498db"}
                rc = risk_colors.get(port.get("risk", "INFO"), "#aaa")
                port_rows_html += f"""
                <tr>
                    <td><code>{host.get('ip','N/A')}</code></td>
                    <td><strong>{port['port']}</strong></td>
                    <td>{port['protocol'].upper()}</td>
                    <td>{port['service']}</td>
                    <td>{port.get('full_version','—')}</td>
                    <td><span class="badge" style="background:{rc}20;color:{rc};border:1px solid {rc}40">{port.get('risk','INFO')}</span></td>
                </tr>"""

        # Build CVE rows
        cve_rows_html = ""
        for service, cve_list in cves.items():
            for cve in cve_list:
                sc = cve.get("severity_color", "#aaa")
                cve_rows_html += f"""
                <tr>
                    <td><a href="{cve['url']}" target="_blank" style="color:#7dd3fc">{cve['id']}</a></td>
                    <td><code style="font-size:11px">{service}</code></td>
                    <td><span class="badge" style="background:{sc}20;color:{sc};border:1px solid {sc}40">{cve.get('severity','?')}</span></td>
                    <td style="color:#f0f0f0">{cve.get('cvss_score','N/A')}</td>
                    <td style="font-size:12px;color:#aaa">{cve.get('description','N/A')}</td>
                </tr>"""

        # Subdomain rows
        sub_rows_html = ""
        for s in subdomains:
            resolved_color = "#2ecc71" if s.get("resolved") else "#e74c3c"
            sub_rows_html += f"""
            <tr>
                <td style="color:#7dd3fc">{s['subdomain']}</td>
                <td><code>{s['ip']}</code></td>
                <td><span style="color:{resolved_color}">{'✓ Resolved' if s.get('resolved') else '✗ Unresolved'}</span></td>
            </tr>"""

        # Host cards
        host_cards_html = ""
        for host in hosts:
            risk_info = next((h for h in risk.get("hosts", []) if h["ip"] == host.get("ip")), {})
            rl = risk_info.get("label", "UNKNOWN")
            rc = risk_info.get("color", "#aaa")
            host_cards_html += f"""
            <div class="host-card">
                <div class="host-header">
                    <div>
                        <div class="host-ip">{host.get('ip','N/A')}</div>
                        <div class="host-meta">{host.get('os','Unknown OS')} · {host.get('os_accuracy','')} confidence</div>
                        <div class="host-meta" style="margin-top:2px">{', '.join(host.get('hostnames',[])) or 'No hostname'}</div>
                    </div>
                    <div style="text-align:right">
                        <div class="risk-badge" style="background:{rc}20;color:{rc};border:1px solid {rc}40;font-size:13px;padding:6px 16px">{rl}</div>
                        <div style="color:#666;font-size:11px;margin-top:4px">Score: {risk_info.get('score',0)}/100</div>
                    </div>
                </div>
                <div style="font-size:12px;color:#888;margin-top:10px">{host.get('open_port_count',0)} open port(s) · {len(host.get('traceroute',[]))} traceroute hop(s)</div>
            </div>"""

        # Diff section
        diff_html = ""
        if diff:
            diff_html = f"""
            <div class="section">
                <div class="section-title">🔄 Scan Diff — Changes Since Last Scan</div>
                <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
                    <div class="stat-card"><div class="stat-num" style="color:#e74c3c">{diff.get('new_ports',0)}</div><div class="stat-label">New Ports</div></div>
                    <div class="stat-card"><div class="stat-num" style="color:#2ecc71">{diff.get('closed_ports',0)}</div><div class="stat-label">Closed Ports</div></div>
                    <div class="stat-card"><div class="stat-num" style="color:#f1c40f">{diff.get('risk_delta',0):+}</div><div class="stat-label">Risk Score Δ</div></div>
                </div>
                <div style="margin-top:12px;font-size:12px;color:#888">Compared to scan from: {diff.get('prev_timestamp','N/A')}</div>
            </div>"""

        # Traceroute
        trace_html = ""
        if hosts and hosts[0].get("traceroute"):
            hops = hosts[0]["traceroute"]
            trace_html = '<div class="traceroute">'
            for i, hop in enumerate(hops):
                trace_html += f'<div class="hop"><div class="hop-ttl">{hop["ttl"]}</div><div class="hop-ip">{hop["ip"]}</div><div style="font-size:10px;color:#666">{hop["rtt"]}ms</div></div>'
                if i < len(hops) - 1:
                    trace_html += '<div style="font-size:18px;color:#444;align-self:center">→</div>'
            trace_html += "</div>"

        whois = whois_dns.get("whois", {})
        dns = whois_dns.get("dns", {})
        dns_sec = dns.get("security", {})

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>NetRecon Report — {target}</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet">
<style>
  :root {{
    --bg: #0a0e1a;
    --bg2: #0f1526;
    --bg3: #151d35;
    --border: #1e2d4d;
    --accent: #3b82f6;
    --accent2: #06b6d4;
    --text: #e2e8f0;
    --text2: #94a3b8;
    --red: #e74c3c;
    --orange: #e67e22;
    --yellow: #f1c40f;
    --green: #2ecc71;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; font-size: 14px; line-height: 1.6; }}
  code, .mono {{ font-family: 'JetBrains Mono', monospace; }}

  /* Header */
  .header {{ background: linear-gradient(135deg, #0a0e1a 0%, #0f1a3d 50%, #0a1628 100%); border-bottom: 1px solid var(--border); padding: 32px 48px; position: relative; overflow: hidden; }}
  .header::before {{ content: ''; position: absolute; top: -50%; left: -10%; width: 60%; height: 200%; background: radial-gradient(ellipse, rgba(59,130,246,0.08) 0%, transparent 70%); pointer-events: none; }}
  .header-grid {{ display: grid; grid-template-columns: 1fr auto; gap: 24px; align-items: center; max-width: 1200px; margin: 0 auto; }}
  .tool-name {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--accent); letter-spacing: .15em; text-transform: uppercase; margin-bottom: 8px; }}
  .header h1 {{ font-size: 28px; font-weight: 600; color: #fff; margin-bottom: 6px; }}
  .header-meta {{ font-size: 12px; color: var(--text2); display: flex; gap: 20px; margin-top: 10px; }}
  .header-meta span {{ display: flex; align-items: center; gap: 5px; }}
  .risk-pill {{ padding: 10px 24px; border-radius: 8px; font-size: 14px; font-weight: 600; letter-spacing: .05em; font-family: 'JetBrains Mono', monospace; }}

  /* Nav */
  .nav {{ background: var(--bg2); border-bottom: 1px solid var(--border); padding: 0 48px; position: sticky; top: 0; z-index: 100; }}
  .nav-inner {{ display: flex; gap: 0; max-width: 1200px; margin: 0 auto; overflow-x: auto; }}
  .nav-link {{ padding: 14px 20px; font-size: 12px; color: var(--text2); text-decoration: none; border-bottom: 2px solid transparent; white-space: nowrap; cursor: pointer; transition: all .2s; }}
  .nav-link:hover, .nav-link.active {{ color: var(--accent); border-bottom-color: var(--accent); }}

  /* Layout */
  .container {{ max-width: 1200px; margin: 0 auto; padding: 32px 48px; }}
  .section {{ background: var(--bg2); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 24px; }}
  .section-title {{ font-size: 13px; font-weight: 600; color: var(--text2); text-transform: uppercase; letter-spacing: .08em; margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }}
  .section-title::after {{ content: ''; flex: 1; height: 1px; background: var(--border); }}

  /* Stats */
  .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px,1fr)); gap: 16px; margin-bottom: 24px; }}
  .stat-card {{ background: var(--bg3); border: 1px solid var(--border); border-radius: 10px; padding: 20px; text-align: center; }}
  .stat-num {{ font-size: 32px; font-weight: 600; font-family: 'JetBrains Mono', monospace; color: var(--accent); }}
  .stat-label {{ font-size: 11px; color: var(--text2); margin-top: 4px; text-transform: uppercase; letter-spacing: .06em; }}

  /* Tables */
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th {{ text-align: left; padding: 10px 14px; background: var(--bg3); color: var(--text2); font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: .06em; border-bottom: 1px solid var(--border); }}
  td {{ padding: 10px 14px; border-bottom: 1px solid rgba(30,45,77,.6); vertical-align: middle; }}
  tr:hover td {{ background: rgba(59,130,246,.04); }}
  tr:last-child td {{ border-bottom: none; }}
  .badge {{ padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 500; font-family: 'JetBrains Mono', monospace; }}

  /* Host cards */
  .host-card {{ background: var(--bg3); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 12px; }}
  .host-header {{ display: flex; justify-content: space-between; align-items: flex-start; }}
  .host-ip {{ font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 500; color: #fff; }}
  .host-meta {{ font-size: 12px; color: var(--text2); margin-top: 3px; }}
  .risk-badge {{ padding: 4px 12px; border-radius: 6px; font-size: 11px; font-weight: 600; font-family: 'JetBrains Mono', monospace; letter-spacing: .06em; display: inline-block; }}

  /* Graph */
  #network-graph {{ width: 100%; height: 480px; background: var(--bg3); border-radius: 8px; border: 1px solid var(--border); }}

  /* Traceroute */
  .traceroute {{ display: flex; align-items: center; flex-wrap: wrap; gap: 6px; }}
  .hop {{ background: var(--bg3); border: 1px solid var(--border); border-radius: 8px; padding: 8px 14px; text-align: center; }}
  .hop-ttl {{ font-size: 10px; color: var(--text2); }}
  .hop-ip {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--accent2); }}

  /* WHOIS grid */
  .info-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 12px; }}
  .info-item {{ background: var(--bg3); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }}
  .info-label {{ font-size: 11px; color: var(--text2); text-transform: uppercase; letter-spacing: .06em; margin-bottom: 4px; }}
  .info-value {{ font-size: 13px; color: var(--text); font-family: 'JetBrains Mono', monospace; word-break: break-all; }}

  /* Executive summary */
  .exec-summary {{ background: linear-gradient(135deg, #0f1a3d, #0a1628); border: 1px solid #1e3a6e; border-radius: 10px; padding: 20px 24px; font-size: 14px; line-height: 1.8; color: #c8d8f0; }}

  /* Footer */
  .footer {{ text-align: center; padding: 32px; color: var(--text2); font-size: 12px; border-top: 1px solid var(--border); margin-top: 32px; }}
  .footer strong {{ color: var(--accent); }}

  /* DNS security */
  .dns-sec {{ display: flex; gap: 12px; flex-wrap: wrap; }}
  .dns-item {{ padding: 8px 16px; border-radius: 8px; font-size: 12px; font-family: 'JetBrains Mono', monospace; }}

  /* Scrollbar */
  ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
  ::-webkit-scrollbar-track {{ background: var(--bg); }}
  ::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}

  @media print {{ .nav {{ display:none; }} .container {{ padding: 16px; }} }}

  /* ── Scroll-reveal ── */
  .section, .stat-card, .host-card {{
    opacity: 0;
    transform: translateY(22px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }}
  .section.visible, .stat-card.visible, .host-card.visible {{
    opacity: 1;
    transform: translateY(0);
  }}
  /* Stagger stat cards */
  .stats-grid .stat-card:nth-child(1) {{ transition-delay: 0.05s; }}
  .stats-grid .stat-card:nth-child(2) {{ transition-delay: 0.10s; }}
  .stats-grid .stat-card:nth-child(3) {{ transition-delay: 0.15s; }}
  .stats-grid .stat-card:nth-child(4) {{ transition-delay: 0.20s; }}
  .stats-grid .stat-card:nth-child(5) {{ transition-delay: 0.25s; }}
  .stats-grid .stat-card:nth-child(6) {{ transition-delay: 0.30s; }}

  /* Nav link hover underline slide */
  .nav-link {{ position: relative; }}
  .nav-link::after {{
    content: '';
    position: absolute;
    bottom: -1px; left: 50%; right: 50%;
    height: 2px;
    background: var(--accent);
    transition: left 0.2s ease, right 0.2s ease;
  }}
  .nav-link:hover::after, .nav-link.active::after {{
    left: 0; right: 0;
  }}
  .nav-link {{ border-bottom: none !important; }}

  /* Table row hover slide-in effect */
  tr {{ transition: background 0.15s; }}

  /* Host card hover lift */
  .host-card {{ transition: opacity 0.5s ease, transform 0.5s ease, box-shadow 0.2s ease, border-color 0.2s ease; cursor: default; }}
  .host-card:hover {{ border-color: #3b82f640; box-shadow: 0 4px 24px rgba(59,130,246,.12); }}
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div class="header-grid">
    <div>
      <div class="tool-name">⬡ NetRecon v1.0 — Network Reconnaissance Report</div>
      <h1>{target}</h1>
      <div class="header-meta">
        <span>📅 {timestamp}</span>
        <span>⚡ {nmap.get('scan_type','normal').upper()} scan</span>
        <span>🖥 {len(hosts)} host(s)</span>
        <span>🔓 {nmap.get('total_ports',0)} open port(s)</span>
        <span>🛡 {total_cves} CVE(s)</span>
      </div>
    </div>
    <div class="risk-pill" style="background:{risk.get('overall_color','#aaa')}20;color:{risk.get('overall_color','#aaa')};border:2px solid {risk.get('overall_color','#aaa')}60">
      {risk.get('overall_label','UNKNOWN')}<br>
      <span style="font-size:11px;opacity:.8">{risk.get('overall_score',0)}/100</span>
    </div>
  </div>
</div>

<!-- NAV -->
<div class="nav">
  <div class="nav-inner">
    <a class="nav-link active" data-section="summary"    onclick="navScrollTo('summary',this)">Summary</a>
    <a class="nav-link"        data-section="graph"      onclick="navScrollTo('graph',this)">Topology</a>
    <a class="nav-link"        data-section="hosts"      onclick="navScrollTo('hosts',this)">Hosts</a>
    <a class="nav-link"        data-section="ports"      onclick="navScrollTo('ports',this)">Ports</a>
    <a class="nav-link"        data-section="cves"       onclick="navScrollTo('cves',this)">CVEs</a>
    <a class="nav-link"        data-section="subdomains" onclick="navScrollTo('subdomains',this)">Subdomains</a>
    <a class="nav-link"        data-section="whois"      onclick="navScrollTo('whois',this)">WHOIS/DNS</a>
    <a class="nav-link"        data-section="traceroute" onclick="navScrollTo('traceroute',this)">Traceroute</a>
  </div>
</div>

<div class="container">

  <!-- STATS -->
  <div class="stats-grid">
    <div class="stat-card"><div class="stat-num">{len(hosts)}</div><div class="stat-label">Hosts</div></div>
    <div class="stat-card"><div class="stat-num">{nmap.get('total_ports',0)}</div><div class="stat-label">Open Ports</div></div>
    <div class="stat-card"><div class="stat-num" style="color:#e74c3c">{critical_count}</div><div class="stat-label">Critical CVEs</div></div>
    <div class="stat-card"><div class="stat-num" style="color:#e67e22">{high_count}</div><div class="stat-label">High CVEs</div></div>
    <div class="stat-card"><div class="stat-num" style="color:#7dd3fc">{len(subdomains)}</div><div class="stat-label">Subdomains</div></div>
    <div class="stat-card"><div class="stat-num" style="color:{risk.get('overall_color','#aaa')}">{risk.get('overall_score',0)}</div><div class="stat-label">Risk Score</div></div>
  </div>

  <!-- EXECUTIVE SUMMARY -->
  <div id="summary" class="section">
    <div class="section-title">📋 Executive Summary</div>
    <div class="exec-summary">{exec_summary}</div>
  </div>

  {diff_html}

  <!-- TOPOLOGY GRAPH -->
  <div id="graph" class="section">
    <div class="section-title">🕸 Network Topology Graph</div>
    <div id="network-graph"></div>
    <div style="margin-top:12px;display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:#888">
      <span>⬤ <span style="color:#3b82f6">Target</span></span>
      <span>⬤ <span style="color:#06b6d4">Host</span></span>
      <span>⬤ <span style="color:#e74c3c">Critical Port</span></span>
      <span>⬤ <span style="color:#e67e22">High Port</span></span>
      <span>⬤ <span style="color:#f1c40f">Medium Port</span></span>
      <span>⬤ <span style="color:#2ecc71">Low/Info Port</span></span>
      <span>⬤ <span style="color:#8b5cf6">Subdomain</span></span>
    </div>
  </div>

  <!-- HOSTS -->
  <div id="hosts" class="section">
    <div class="section-title">🖥 Discovered Hosts</div>
    {host_cards_html or '<div style="color:#666;font-size:13px">No hosts discovered</div>'}
  </div>

  <!-- PORTS -->
  <div id="ports" class="section">
    <div class="section-title">🔓 Open Ports & Services</div>
    <div style="overflow-x:auto">
    <table>
      <tr><th>Host</th><th>Port</th><th>Proto</th><th>Service</th><th>Version</th><th>Risk</th></tr>
      {port_rows_html or '<tr><td colspan="6" style="color:#666;text-align:center">No open ports found</td></tr>'}
    </table>
    </div>
  </div>

  <!-- CVEs -->
  <div id="cves" class="section">
    <div class="section-title">🛡 CVE Vulnerability Matches</div>
    <div style="overflow-x:auto">
    <table>
      <tr><th>CVE ID</th><th>Service</th><th>Severity</th><th>CVSS</th><th>Description</th></tr>
      {cve_rows_html or '<tr><td colspan="5" style="color:#666;text-align:center">No CVEs found or CVE lookup skipped</td></tr>'}
    </table>
    </div>
  </div>

  <!-- SUBDOMAINS -->
  <div id="subdomains" class="section">
    <div class="section-title">🌐 Subdomain Enumeration</div>
    <div style="overflow-x:auto">
    <table>
      <tr><th>Subdomain</th><th>IP</th><th>Status</th></tr>
      {sub_rows_html or '<tr><td colspan="3" style="color:#666;text-align:center">No subdomains found or enumeration skipped</td></tr>'}
    </table>
    </div>
  </div>

  <!-- WHOIS / DNS -->
  <div id="whois" class="section">
    <div class="section-title">🔍 WHOIS & DNS Intelligence</div>
    <div class="info-grid" style="margin-bottom:20px">
      <div class="info-item"><div class="info-label">Registrant</div><div class="info-value">{whois.get('registrant','N/A')}</div></div>
      <div class="info-item"><div class="info-label">Registrar</div><div class="info-value">{whois.get('registrar','N/A')}</div></div>
      <div class="info-item"><div class="info-label">Created</div><div class="info-value">{whois.get('created','N/A')}</div></div>
      <div class="info-item"><div class="info-label">Expires</div><div class="info-value">{whois.get('expires','N/A')}</div></div>
      <div class="info-item"><div class="info-label">Country</div><div class="info-value">{whois.get('country','N/A')}</div></div>
      <div class="info-item"><div class="info-label">Status</div><div class="info-value">{whois.get('status','N/A')[:60]}</div></div>
    </div>
    <div class="section-title" style="margin-top:16px">Email Security (SPF / DMARC)</div>
    <div class="dns-sec">
      <div class="dns-item" style="background:{'#1a3a2a' if 'Present' in dns_sec.get('spf','') else '#3a1a1a'};color:{'#2ecc71' if 'Present' in dns_sec.get('spf','') else '#e74c3c'}">
        SPF: {dns_sec.get('spf','Unknown')}
      </div>
      <div class="dns-item" style="background:{'#1a3a2a' if 'Present' in dns_sec.get('dmarc','') else '#3a1a1a'};color:{'#2ecc71' if 'Present' in dns_sec.get('dmarc','') else '#e74c3c'}">
        DMARC: {dns_sec.get('dmarc','Unknown')}
      </div>
    </div>
  </div>

  <!-- TRACEROUTE -->
  <div id="traceroute" class="section">
    <div class="section-title">📡 Traceroute Path</div>
    {trace_html or '<div style="color:#666;font-size:13px">No traceroute data (enable with normal/aggressive scan)</div>'}
  </div>

</div>

<!-- FOOTER -->
<div class="footer">
  Generated by <strong>NetRecon v1.0</strong> — BTech Cybersecurity Capstone Project &nbsp;|&nbsp;
  Scan completed: {timestamp} &nbsp;|&nbsp;
  <span style="color:#e74c3c">For authorized use only</span>
</div>

<script>
// ── Nav scroll & active state ─────────────────────────────────────────────
function navScrollTo(id, el) {{
  const target = document.getElementById(id);
  if (!target) return;
  const navH = document.querySelector('.nav')?.offsetHeight || 56;
  const top = target.getBoundingClientRect().top + window.pageYOffset - navH - 12;
  window.scrollTo({{ top: top, behavior: 'smooth' }});
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  el.classList.add('active');
}}

// ── Scroll-spy: highlight correct nav link as user scrolls ────────────────
const sections = ['summary','graph','hosts','ports','cves','subdomains','whois','traceroute'];
const navLinks = {{}};
sections.forEach(id => {{
  const el = document.querySelector(`.nav-link[data-section="${{id}}"]`);
  if (el) navLinks[id] = el;
}});

function updateActivLink() {{
  const navH = document.querySelector('.nav')?.offsetHeight || 56;
  let current = sections[0];
  sections.forEach(id => {{
    const el = document.getElementById(id);
    if (el && el.getBoundingClientRect().top - navH - 30 <= 0) current = id;
  }});
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  if (navLinks[current]) navLinks[current].classList.add('active');
}}
window.addEventListener('scroll', updateActivLink, {{ passive: true }});

// ── Scroll-reveal: fade sections in as they enter viewport ────────────────
const revealEls = document.querySelectorAll('.section, .stat-card, .host-card');
const io = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{
      e.target.classList.add('visible');
      io.unobserve(e.target);
    }}
  }});
}}, {{ threshold: 0.08 }});
revealEls.forEach(el => io.observe(el));

// ── Topology graph ────────────────────────────────────────────────────────
const nodes = new vis.DataSet({graph_nodes});
const edges = new vis.DataSet({graph_edges});

const groupColors = {{
  target:    {{ color: {{ background: '#3b82f6', border: '#60a5fa' }}, font: {{ color: '#fff', size: 14, bold: true }} }},
  host:      {{ color: {{ background: '#0e7490', border: '#06b6d4' }}, font: {{ color: '#fff', size: 12 }} }},
  critical:  {{ color: {{ background: '#7f1d1d', border: '#e74c3c' }}, font: {{ color: '#fca5a5', size: 11 }} }},
  high:      {{ color: {{ background: '#7c3a1e', border: '#e67e22' }}, font: {{ color: '#fdba74', size: 11 }} }},
  medium:    {{ color: {{ background: '#713f12', border: '#f1c40f' }}, font: {{ color: '#fef08a', size: 11 }} }},
  low:       {{ color: {{ background: '#14532d', border: '#2ecc71' }}, font: {{ color: '#86efac', size: 11 }} }},
  info:      {{ color: {{ background: '#1e3a5f', border: '#3b82f6' }}, font: {{ color: '#93c5fd', size: 11 }} }},
  subdomain: {{ color: {{ background: '#4c1d95', border: '#8b5cf6' }}, font: {{ color: '#c4b5fd', size: 11 }} }},
}};

const options = {{
  nodes: {{ shape: 'dot', borderWidth: 2, shadow: true }},
  edges: {{ color: {{ color: '#1e3a5f', highlight: '#3b82f6' }}, smooth: {{ type: 'continuous' }}, width: 1.5, arrows: {{ to: {{ enabled: true, scaleFactor: 0.5 }} }} }},
  groups: groupColors,
  physics: {{ stabilization: {{ iterations: 150 }}, barnesHut: {{ gravitationalConstant: -8000, springLength: 120 }} }},
  interaction: {{ hover: true, tooltipDelay: 200, navigationButtons: true }},
}};

const container = document.getElementById('network-graph');
new vis.Network(container, {{ nodes, edges }}, options);

// ── Counter animation for stat numbers ────────────────────────────────────
function animateCounter(el) {{
  const target = parseInt(el.textContent, 10);
  if (isNaN(target) || target === 0) return;
  let current = 0;
  const step = Math.max(1, Math.floor(target / 30));
  const timer = setInterval(() => {{
    current = Math.min(current + step, target);
    el.textContent = current;
    if (current >= target) clearInterval(timer);
  }}, 30);
}}
document.querySelectorAll('.stat-num').forEach(el => {{
  const statIo = new IntersectionObserver((entries) => {{
    if (entries[0].isIntersecting) {{ animateCounter(el); statIo.disconnect(); }}
  }}, {{ threshold: 0.5 }});
  statIo.observe(el);
}});
</script>
</body>
</html>"""
