<div align="center">

<br>

```
 ███╗   ██╗███████╗████████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
 ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
 ██╔██╗ ██║█████╗     ██║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
 ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
 ██║ ╚████║███████╗   ██║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

**Advanced Network Reconnaissance & Visual Reporting Tool**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-557C94?style=flat-square&logo=kalilinux)](https://kali.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()
[![Capstone](https://img.shields.io/badge/BTech-Capstone%20Project-orange?style=flat-square)]()

*A single command. A complete picture of your target.*

</div>

---

## What is NetRecon?

**NetRecon** is a full-spectrum network reconnaissance and reporting framework built on Kali Linux. It combines active scanning via Nmap with passive OSINT enrichment from WHOIS, DNS, NVD, and Shodan — then compiles everything into a **professional, interactive HTML/PDF report** with a Maltego-style network topology graph.

Built as a BTech Cybersecurity capstone project, NetRecon bridges the gap between raw scanner output and analyst-ready intelligence reports. Instead of reading walls of terminal text, you get a visual, structured, risk-scored report that any security analyst — or client — can act on immediately.

> ⚠️ **Legal Notice:** NetRecon is built for authorized security assessments only. Never scan systems you do not own or have explicit written permission to test. The author assumes no liability for misuse.

---

## Demo

```
$ python3 recon.py -t scanme.nmap.org -i normal -o demo_report

  [*] Target: scanme.nmap.org
  [*] Intensity: normal | Format: html
  [*] Started at: 2024-11-15 14:32:11

  [*] Running nmap scan...
  [+] Discovered 1 host(s), 4 open port(s)
  [*] Fetching WHOIS & DNS records...
  [+] WHOIS & DNS enrichment complete
  [*] Looking up CVEs via NVD API...
  [+] Found 3 CVE(s) across all services
  [*] Enumerating subdomains...
  [+] Found 6 subdomain(s)
  [*] Calculating risk scores...
  [+] Overall risk: HIGH
  [*] Saving to scan history...
  [*] Generating report...
  [+] HTML report saved: output/demo_report_20241115_143211.html

  [+] Scan complete!
```

---

## Features

### 🔍 Active Reconnaissance
- **Deep Nmap scanning** — service version detection (`-sV`), OS fingerprinting (`-O`), default scripts (`-sC`), aggressive enumeration (`-A`), and NSE vulnerability scripts
- Three intensity modes: **Quick**, **Normal**, **Aggressive** — each with appropriate Nmap flags
- Full **traceroute** path capture from scanner to target

### 🌐 Passive OSINT Enrichment
- **WHOIS lookup** — registrant, registrar, creation/expiry dates, name servers, domain status
- **DNS enumeration** — A, AAAA, MX, NS, TXT, SOA records with SPF/DMARC security checks
- **Shodan integration** — cross-reference indexed banners, geolocation, ISP, and tagged vulnerabilities (API key required)

### 🛡 Vulnerability Intelligence
- **NVD CVE lookup** — automatically maps each detected service version to real CVE IDs with CVSS scores, severity ratings, and direct links to the National Vulnerability Database
- Risk classification: **Critical / High / Medium / Low** per service

### 🧮 Risk Scoring Engine
- Weighted scoring algorithm per host based on: dangerous open ports, CVSS scores, Shodan vulnerability tags
- Per-host and overall risk scores (0–100) with labeled badges

### 🕸 Visual Topology Graph
- **Interactive Maltego-style node graph** built with vis.js
- Target → Hosts → Ports → Services → CVEs → Subdomains all represented as color-coded, draggable, zoomable nodes

### 📁 Subdomain Enumeration
- Integrates with **subfinder** (Kali) for passive subdomain discovery
- Fallback wordlist-based DNS brute-force for offline environments
- Each discovered subdomain resolved to IP and added to the graph

### 🕓 Scan History & Diff
- Every scan stored in a local **SQLite database**
- Re-scanning the same target produces a **diff report** — new ports, closed ports, risk score delta
- Enables continuous monitoring and attack surface tracking over time

### 📊 Professional Report Output
- **Self-contained HTML report** — no external dependencies, single file, works offline
- Auto-generated **plain-English executive summary** paragraph
- Clean tables for ports, CVEs, subdomains, WHOIS, DNS security
- **PDF export** via wkhtmltopdf

---

## Report Structure

| Section | Content |
|---|---|
| Executive Summary | Plain-English findings overview |
| Risk Dashboard | Score cards — hosts, ports, CVEs, subdomains |
| Network Topology | Interactive vis.js node graph |
| Host Overview | Per-host cards with OS, risk, port count |
| Open Ports & Services | Full port table with versions and risk badges |
| CVE Matches | NVD-sourced vulnerabilities with CVSS scores |
| Subdomain Map | Discovered subdomains with IP resolution |
| WHOIS / DNS | Domain ownership + SPF/DMARC checks |
| Traceroute | Network path hop visualization |
| Scan Diff | Changes since last scan (if applicable) |

---

## Project Structure

```
NetRecon/
├── recon.py                  # Main entry point & CLI
├── requirements.txt          # Python dependencies
├── modules/
│   ├── scanner.py            # Nmap scanning engine & XML parser
│   ├── whois_dns.py          # WHOIS & DNS enrichment
│   ├── cve_lookup.py         # NVD API CVE mapping
│   ├── shodan_lookup.py      # Shodan passive enrichment
│   ├── subdomain_enum.py     # Subdomain discovery & resolution
│   ├── risk_scorer.py        # Weighted risk scoring engine
│   ├── history.py            # SQLite scan history & diff engine
│   └── report_gen.py         # HTML/PDF report generator
└── output/                   # Generated reports & history DB
```

---

## Installation

**Prerequisites:** Kali Linux (recommended) or any Linux with nmap installed.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/NetRecon.git
cd NetRecon

# 2. Install Python dependencies
pip3 install -r requirements.txt --break-system-packages

# 3. (Optional) Install subfinder for subdomain enumeration
sudo apt install -y subfinder

# 4. (Optional) Install wkhtmltopdf for PDF export
sudo apt install -y wkhtmltopdf

# 5. Make the script executable
chmod +x recon.py
```

---

## Usage

### Basic scan
```bash
python3 recon.py -t 192.168.1.1
```

### Scan a domain with aggressive mode
```bash
python3 recon.py -t example.com -i aggressive -o my_report
```

### Scan with Shodan enrichment
```bash
python3 recon.py -t 192.168.1.1 --shodan-key YOUR_API_KEY
```

### Generate HTML + PDF
```bash
python3 recon.py -t 192.168.1.0/24 --format both -o subnet_audit
```

### Quick scan (skip CVEs and subdomains)
```bash
python3 recon.py -t 10.0.0.1 -i quick --no-cve --no-subdomains
```

### Full command reference
```
usage: recon.py [-h] -t TARGET [-o OUTPUT] [-i {quick,normal,aggressive}]
                [--shodan-key KEY] [--no-cve] [--no-subdomains]
                [--format {html,both}] [--history]

  -t, --target          Target IP, hostname, or CIDR (required)
  -o, --output          Output filename without extension (default: netrecon_report)
  -i, --intensity       Scan intensity: quick | normal | aggressive (default: normal)
  --shodan-key          Shodan API key for passive enrichment
  --no-cve              Skip CVE lookup
  --no-subdomains       Skip subdomain enumeration
  --format              Output format: html | both (html + pdf)
  --history             Show scan history and diff for target
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Active Scanning | Nmap + NSE Scripts |
| XML Parsing | Python `xml.etree` |
| WHOIS Lookup | `python-whois` + system `whois` |
| DNS Records | `dnspython` + `dig` |
| CVE Data | NVD REST API v2.0 |
| Shodan Data | Shodan API |
| Subdomain Enum | subfinder + DNS brute-force |
| Scan History | SQLite3 |
| Report Templating | Python f-strings (Jinja2-ready) |
| Topology Graph | vis.js |
| PDF Export | wkhtmltopdf |
| CLI | Python argparse |

---

## Limitations & Responsible Use

- Always run on networks and systems **you own or are explicitly authorized to test**
- Aggressive scans may trigger IDS/IPS alerts on monitored networks
- Shodan and NVD API calls require internet access
- CVE matching is keyword-based — verify critical findings manually
- This tool is intended for **educational and authorized professional use only**

---

## Future Roadmap

- [ ] Web UI dashboard (Flask)
- [ ] Automated screenshot of web services (Selenium)
- [ ] Metasploit module suggestion based on CVEs
- [ ] Email notification on risk score change
- [ ] Docker container for portable deployment
- [ ] Multi-target parallel scanning

---

## About

Developed by **[R.Shasi Kiran]** as a BTech Cybersecurity project.

- 🎓 BTech Cybersecurity — [Lovely Professional University]
- 📧 [shashikiranreyya@gmail.com]
- 🔗 [linkedin.com/in/reyya-shasi-kiran116]

---

<div align="center">

**⭐ Star this repo if you found it useful**

*Built with ❤️ on Kali Linux*

</div>
