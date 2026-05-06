[🌐 View Project Page](https://rshasikiran.github.io/NetRecon/)

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="100%">
  <defs>
    <!-- Deep dark gradient background -->
    <linearGradient id="hbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#010b18"/>
      <stop offset="40%"  stop-color="#051728"/>
      <stop offset="80%"  stop-color="#0b2d4e"/>
      <stop offset="100%" stop-color="#010b18"/>
    </linearGradient>
    <!-- Cyan glow for title -->
    <linearGradient id="titlegrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#00aaff"/>
      <stop offset="50%"  stop-color="#00ffee"/>
      <stop offset="100%" stop-color="#00aaff"/>
    </linearGradient>
    <!-- Glow filter for text -->
    <filter id="glow" x="-20%" y="-40%" width="140%" height="180%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Stronger outer glow for title -->
    <filter id="titleglow" x="-10%" y="-60%" width="120%" height="220%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="blur1"/>
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur1"/>
        <feMergeNode in="blur2"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <!-- Subtle grid pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#00d4ff" stroke-width="0.15" stroke-opacity="0.18"/>
    </pattern>
    <!-- Radial glow behind title -->
    <radialGradient id="centerglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#00d4ff" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </radialGradient>
    <!-- Wave gradients -->
    <linearGradient id="wgrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#00d4ff" stop-opacity="0"/>
      <stop offset="30%"  stop-color="#00d4ff" stop-opacity="0.5"/>
      <stop offset="70%"  stop-color="#0080ff" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="wgrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#0055ff" stop-opacity="0"/>
      <stop offset="50%"  stop-color="#00eeff" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0055ff" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- ── Base background ── -->
  <rect width="900" height="280" fill="url(#hbg)"/>

  <!-- ── Grid overlay ── -->
  <rect width="900" height="280" fill="url(#grid)"/>

  <!-- ── Center radial glow ── -->
  <ellipse cx="450" cy="140" rx="380" ry="120" fill="url(#centerglow)"/>

  <!-- ── Circuit lines — left side ── -->
  <g stroke="#00d4ff" stroke-opacity="0.22" stroke-width="1" fill="none">
    <polyline points="0,60 80,60 80,90 160,90"/>
    <polyline points="0,100 50,100 50,130 120,130 120,110 200,110"/>
    <polyline points="0,180 70,180 70,160 150,160"/>
    <polyline points="0,220 90,220 90,200 180,200 180,215 240,215"/>
    <circle cx="80"  cy="60"  r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="50"  cy="100" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="120" cy="130" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="70"  cy="180" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="90"  cy="220" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="180" cy="200" r="3" fill="#00ffee" stroke="none" opacity="0.7"/>
  </g>

  <!-- ── Circuit lines — right side (mirrored) ── -->
  <g stroke="#00d4ff" stroke-opacity="0.22" stroke-width="1" fill="none">
    <polyline points="900,60 820,60 820,90 740,90"/>
    <polyline points="900,100 850,100 850,130 780,130 780,110 700,110"/>
    <polyline points="900,180 830,180 830,160 750,160"/>
    <polyline points="900,220 810,220 810,200 720,200 720,215 660,215"/>
    <circle cx="820" cy="60"  r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="850" cy="100" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="780" cy="130" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="830" cy="180" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="810" cy="220" r="3" fill="#00d4ff" stroke="none" opacity="0.6"/>
    <circle cx="720" cy="200" r="3" fill="#00ffee" stroke="none" opacity="0.7"/>
  </g>

  <!-- ── Horizontal scan line ── -->
  <rect x="0" y="139" width="900" height="1" fill="url(#wgrad1)" opacity="0.6"/>
  <rect x="0" y="141" width="900" height="1" fill="url(#wgrad2)" opacity="0.4"/>

  <!-- ── Top decorative bar ── -->
  <rect x="0" y="0" width="900" height="3" fill="url(#wgrad1)"/>

  <!-- ── Bottom wave shapes ── -->
  <path d="M0,230 C120,210 240,250 360,225 C480,200 600,240 720,218 C810,200 870,225 900,215 L900,280 L0,280 Z"
        fill="#00d4ff" fill-opacity="0.06"/>
  <path d="M0,250 C150,235 300,260 450,245 C600,230 750,258 900,242 L900,280 L0,280 Z"
        fill="#0055ff" fill-opacity="0.08"/>

  <!-- ── Bottom decorative bar ── -->
  <rect x="0" y="277" width="900" height="3" fill="url(#wgrad1)"/>

  <!-- ── Corner brackets ── -->
  <g stroke="#00d4ff" stroke-width="2" stroke-opacity="0.7" fill="none">
    <polyline points="20,20 20,8 32,8"/>
    <polyline points="868,8 880,8 880,20"/>
    <polyline points="20,260 20,272 32,272"/>
    <polyline points="868,272 880,272 880,260"/>
  </g>

  <!-- ── Small scanning dots (decorative) ── -->
  <g fill="#00ffee" opacity="0.5">
    <circle cx="42"  cy="18"  r="2"/>
    <circle cx="52"  cy="18"  r="2"/>
    <circle cx="62"  cy="18"  r="2"/>
    <circle cx="838" cy="18"  r="2"/>
    <circle cx="848" cy="18"  r="2"/>
    <circle cx="858" cy="18"  r="2"/>
  </g>

  <!-- ── NETRECON title — shadow/glow layer ── -->
  <text x="450" y="118"
        font-family="'Courier New', Courier, monospace"
        font-size="78" font-weight="bold"
        fill="#00d4ff" fill-opacity="0.18"
        text-anchor="middle" letter-spacing="10">NETRECON</text>

  <!-- ── NETRECON title — main glowing text ── -->
  <text x="450" y="115"
        font-family="'Courier New', Courier, monospace"
        font-size="78" font-weight="bold"
        fill="url(#titlegrad)"
        text-anchor="middle" letter-spacing="10"
        filter="url(#titleglow)">NETRECON</text>

  <!-- ── Divider lines flanking subtitle ── -->
  <line x1="55"  y1="140" x2="265" y2="140" stroke="url(#wgrad1)" stroke-width="1"/>
  <line x1="635" y1="140" x2="845" y2="140" stroke="url(#wgrad1)" stroke-width="1"/>

  <!-- ── Diamond ornaments ── -->
  <polygon points="280,140 287,133 294,140 287,147" fill="#00d4ff" opacity="0.7"/>
  <polygon points="606,140 613,133 620,140 613,147" fill="#00d4ff" opacity="0.7"/>

  <!-- ── Subtitle text ── -->
  <text x="450" y="146"
        font-family="'Courier New', Courier, monospace"
        font-size="12.5" fill="#7ecfff"
        text-anchor="middle" letter-spacing="3.5"
        filter="url(#glow)">ADVANCED NETWORK RECONNAISSANCE &amp; VISUAL REPORTING</text>

  <!-- ── ASCII-style tag line ── -->
  <text x="450" y="180"
        font-family="'Courier New', Courier, monospace"
        font-size="11" fill="#00ffaa"
        text-anchor="middle" letter-spacing="2" opacity="0.85">⬡  SCAN  ·  ENRICH  ·  SCORE  ·  REPORT  ⬡</text>

  <!-- ── Version tag ── -->
  <rect x="380" y="195" width="140" height="22" rx="4"
        fill="#00d4ff" fill-opacity="0.08" stroke="#00d4ff" stroke-opacity="0.3" stroke-width="1"/>
  <text x="450" y="210"
        font-family="'Courier New', Courier, monospace"
        font-size="10" fill="#00d4ff"
        text-anchor="middle" letter-spacing="2" opacity="0.9">v1.0  ·  KALI LINUX  ·  MIT</text>

  <!-- ── Blinking-style dot indicators (decorative) ── -->
  <circle cx="450" cy="240" r="2.5" fill="#00ff88" opacity="0.9"/>
  <circle cx="440" cy="240" r="1.8" fill="#00d4ff" opacity="0.5"/>
  <circle cx="460" cy="240" r="1.8" fill="#00d4ff" opacity="0.5"/>
  <circle cx="430" cy="240" r="1.2" fill="#00d4ff" opacity="0.3"/>
  <circle cx="470" cy="240" r="1.2" fill="#00d4ff" opacity="0.3"/>
</svg>

<br>

<!-- ASCII banner — centered, full-width SVG so it renders perfectly on GitHub -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 105" width="100%">
  <defs>
    <linearGradient id="asciibg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#010b18"/>
      <stop offset="100%" stop-color="#051728"/>
    </linearGradient>
    <linearGradient id="asciitext" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#0077cc"/>
      <stop offset="40%"  stop-color="#00d4ff"/>
      <stop offset="60%"  stop-color="#00ffee"/>
      <stop offset="100%" stop-color="#0077cc"/>
    </linearGradient>
    <filter id="aglow">
      <feGaussianBlur in="SourceGraphic" stdDeviation="1.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="900" height="105" fill="url(#asciibg)"/>
  <rect x="0" y="0"   width="900" height="1" fill="#00d4ff" opacity="0.15"/>
  <rect x="0" y="104" width="900" height="1" fill="#00d4ff" opacity="0.15"/>
  <text font-family="'Courier New', Courier, monospace" font-size="11.2"
        fill="url(#asciitext)" text-anchor="middle" filter="url(#aglow)" letter-spacing="0.5">
    <tspan x="450" dy="17">███╗   ██╗███████╗████████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗</tspan>
    <tspan x="450" dy="14">████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║</tspan>
    <tspan x="450" dy="14">██╔██╗ ██║█████╗     ██║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║</tspan>
    <tspan x="450" dy="14">██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║</tspan>
    <tspan x="450" dy="14">██║ ╚████║███████╗   ██║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║</tspan>
    <tspan x="450" dy="14">╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝</tspan>
  </text>
</svg>

<br>

[![Python](https://img.shields.io/badge/Python-3.8%2B-00d4ff?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Kali_Linux-Ready-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)](https://kali.org)
[![Nmap](https://img.shields.io/badge/Powered_by-Nmap-ff6b00?style=for-the-badge&logoColor=white)](https://nmap.org)
[![NVD](https://img.shields.io/badge/CVE_Data-NVD_API-ff3366?style=for-the-badge&logoColor=white)](https://nvd.nist.gov)
[![License](https://img.shields.io/badge/License-MIT-00ff88?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-00ff88?style=for-the-badge)]()
[![LOC](https://img.shields.io/badge/Lines_of_Code-1417%2B-8b5cf6?style=for-the-badge)]()
[![Modules](https://img.shields.io/badge/Modules-8-f59e0b?style=for-the-badge)]()

<br>

> **⬡ ONE COMMAND · COMPLETE PICTURE OF YOUR TARGET ⬡**
>
> *Scan → Enrich → Score → Report — fully automated on Kali Linux*

<br>

</div>

---

<div align="center">

## ⚡ The Problem NetRecon Solves

</div>

Every time you start a pentest, CTF, or network audit — you have to manually run nmap, then separately run whois, then dig, then look up CVEs one by one, then check Shodan, then write a report yourself. That's 5 different tools and 30+ minutes before you even start analyzing.

**NetRecon collapses all of that into one command.**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  WITHOUT NETRECON              │  WITH NETRECON                         │
│────────────────────────────────│────────────────────────────────────────│
│  $ nmap -sV 192.168.1.1        │  $ sudo python3 recon.py -t target.com │
│  [wall of text...]             │                                        │
│  $ whois target.com            │  [*] Nmap scan running...              │
│  [more text...]                │  [+] 6 open ports found                │
│  $ dig ANY target.com          │  [+] 3 CVEs found — 2 CRITICAL         │
│  [even more text...]           │  [+] 6 subdomains discovered           │
│  $ manually search CVEs...     │  [+] Risk Score: 95/100 — CRITICAL     │
│  $ write your own report...    │  [+] Report ready → open in browser    │
│                                │                                        │
│  ⏱ 30+ minutes of manual work  │  ⏱ One command. Done.                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

<div align="center">

## 🗺️ How It Works — Automated Pipeline

</div>

<div align="center">

![NetRecon Workflow](assets/workflow.svg)

</div>

The tool runs in **8 automatic phases** — you give it a target and wait for the report.

```
 Target Input
      │
      ▼
 Phase 1 ── Nmap Scan (scanner.py)
      │        Runs nmap -sV -sC -O -A --traceroute, parses XML output
      ▼
 Phase 2 ── WHOIS + DNS (whois_dns.py)
      │        Registrar · DNS A/MX/TXT/NS records · SPF · DMARC
      ▼
 Phase 3 ── Shodan Passive Intel (shodan_lookup.py)
      │        ISP · Location · Historical ports · Tagged vulns
      ▼
 Phase 4 ── CVE Lookup (cve_lookup.py)
      │        NVD API v2.0 · CVSS scores · Severity ratings
      ▼
 Phase 5 ── Subdomain Enumeration (subdomain_enum.py)
      │        subfinder → DNS brute-force fallback → IP resolution
      ▼
 Phase 6 ── Risk Scoring (risk_scorer.py)
      │        Weighted algorithm → 0–100 score → Critical/High/Med/Low
      ▼
 Phase 7 ── History & Diff (history.py)
      │        SQLite3 database · Port diff vs last scan
      ▼
 Phase 8 ── Report Generation (report_gen.py)
               HTML + vis.js topology graph + optional PDF
```

---

<div align="center">

## 🧩 Features

</div>

<table>
<tr>
<td width="50%">

**🔎 Nmap Scan Engine**
Runs nmap in quick, normal, or aggressive mode. Discovers open ports, exact service versions, OS fingerprint with accuracy %, MAC vendor, and full traceroute hops to the target. Parses nmap XML output directly for clean structured data.

</td>
<td width="50%">

**📋 WHOIS + DNS Lookup**
Fetches domain ownership, registrar, creation/expiry dates, country, and name servers via the system `whois` command. Queries all DNS record types (A, AAAA, MX, NS, TXT, SOA) using `dig`. Checks SPF and DMARC — flags missing email security as a phishing/spoofing risk.

</td>
</tr>
<tr>
<td>

**🛡️ CVE Vulnerability Mapping**
For every service + version string detected by nmap, queries the NVD REST API v2.0 and returns real CVE IDs with CVSS scores, severity ratings (Critical/High/Medium/Low), English descriptions, and direct NVD links. Respects NVD's rate limit with a built-in 0.6s delay between requests.

</td>
<td>

**👁️ Shodan Passive Intel**
Queries Shodan without touching the target at all — completely passive. Returns org, ISP, geolocation (city, country, lat/lon), ASN, historically seen ports, OS tags, hostnames, and any CVEs Shodan has already tagged against the IP.

</td>
</tr>
<tr>
<td>

**🌐 Subdomain Enumeration**
Runs `subfinder` first for passive discovery, then automatically falls back to DNS brute-force (www, mail, api, dev, staging, admin, vpn, etc.) if subfinder isn't available. Resolves every found subdomain to its IP and caps results at 50 to keep things manageable.

</td>
<td>

**📊 Risk Scoring Engine**
Custom weighted scoring: Telnet open = +40, RDP = +35, SMB = +35, VNC = +25, FTP = +20, each CVE scores `CVSS × 2` points, each Shodan-tagged vuln = +10. Score is capped at 100 and mapped to Critical / High / Medium / Low with color codes for the report.

</td>
</tr>
<tr>
<td>

**🕓 Scan History & Diff**
Every scan is stored in a local SQLite3 database (`output/netrecon_history.db`). Re-scanning the same target shows exactly what changed: new ports opened, closed ports, and the risk score delta vs the previous scan — useful for tracking patch progress.

</td>
<td>

**🕸️ Maltego-Style Topology Graph**
Interactive vis.js network graph embedded directly in the HTML report. Target in the center, each open port as a draggable color-coded node. Drag, zoom, and click nodes — no extra install needed, loads vis.js from CDN.

</td>
</tr>
</table>

---

<div align="center">

## 📊 Risk Scoring System

</div>

The scoring engine (`risk_scorer.py`) assigns every discovered host a score from 0 to 100:

```
┌──────────────────────────────────────────────────────────────────────────┐
│  SCORE    LABEL      COLOR     WHAT IT MEANS                             │
│──────────────────────────────────────────────────────────────────────────│
│  80–100   CRITICAL   🔴 Red    Telnet/RDP/SMB open + exploitable CVEs    │
│  55–79    HIGH       🟠 Orange  High-risk ports + high CVSS CVEs          │
│  30–54    MEDIUM     🟡 Yellow  Some exposure, medium severity findings   │
│  0–29     LOW        🟢 Green   Minimal exposure, no critical CVEs        │
└──────────────────────────────────────────────────────────────────────────┘

  Port scoring weights (from risk_scorer.py):
  ├── Port 23   (Telnet)    open  →  +40 pts   ← plaintext, often exploitable
  ├── Port 3389 (RDP)       open  →  +35 pts   ← BlueKeep, ransomware entry
  ├── Port 445  (SMB)       open  →  +35 pts   ← EternalBlue / WannaCry
  ├── Port 135  (RPC)       open  →  +25 pts
  ├── Port 139  (NetBIOS)   open  →  +25 pts
  ├── Port 5900 (VNC)       open  →  +25 pts
  ├── Port 1433 (MSSQL)     open  →  +25 pts
  ├── Port 21   (FTP)       open  →  +20 pts   ← anonymous login risk
  ├── Port 3306 (MySQL)     open  →  +20 pts
  ├── Port 27017 (MongoDB)  open  →  +20 pts
  ├── Port 6379 (Redis)     open  →  +20 pts
  ├── Port 25   (SMTP)      open  →  +15 pts
  ├── Port 110  (POP3)      open  →  +15 pts
  ├── CVE found (CVSS 9.8)        →  +19 pts   ← score = CVSS × 2
  └── Shodan vuln tag             →  +10 pts each
```

---

<div align="center">

## 📁 Project Structure

</div>

```
NetRecon/
│
├── recon.py               ← START HERE — orchestrates all 8 phases
├── install.sh             ← run once to install all dependencies on Kali
├── requirements.txt       ← Python packages (python-whois, dnspython, requests)
├── README.md              ← this file
├── LICENSE                ← MIT
│
├── modules/
│   ├── __init__.py        ← marks modules/ as a Python package (must exist)
│   ├── scanner.py         ← NmapScanner class — runs nmap, parses XML
│   ├── whois_dns.py       ← WhoisDNS class — whois + dig + SPF/DMARC
│   ├── cve_lookup.py      ← CVELookup class — NVD API v2.0 queries
│   ├── shodan_lookup.py   ← ShodanLookup class — Shodan REST API
│   ├── subdomain_enum.py  ← SubdomainEnum class — subfinder + brute-force
│   ├── risk_scorer.py     ← RiskScorer class — weighted 0–100 scoring
│   ├── history.py         ← ScanHistory class — SQLite + diff engine
│   └── report_gen.py      ← ReportGenerator class — HTML + PDF output
│
└── output/
    ├── demo_report.html        ← pre-generated sample report (open in browser)
    └── netrecon_history.db     ← SQLite history database (auto-created on first run)
```

---

<div align="center">

## 🚀 Installation — Kali Linux

</div>

### Step 1 — Clone the repository

```bash
git clone https://github.com/RShasikiran/NetRecon.git
cd NetRecon
```

### Step 2 — Run the installer (one time only)

```bash
sudo bash install.sh
```

The installer handles everything automatically:

```
[✓] nmap installed
[✓] whois installed
[✓] dnsutils installed
[✓] subfinder installed
[✓] wkhtmltopdf installed
[✓] python-whois installed
[✓] dnspython installed
[✓] output/ directory ready
[✓] recon.py is executable
[✓] All dependencies satisfied. Ready to run!
```

### Step 3 — Run your first scan

```bash
# scanme.nmap.org is Nmap's official legal sandbox — always safe to scan
sudo python3 recon.py -t scanme.nmap.org -i normal
```

### Step 4 — Open the report

```bash
firefox output/netrecon_report_*.html
```

---

<div align="center">

## 💻 Usage

</div>

```bash
# Basic — scan a single IP, normal intensity
sudo python3 recon.py -t 192.168.1.1

# Scan a domain with custom output filename
sudo python3 recon.py -t example.com -i normal -o my_audit

# Aggressive deep scan — all 65535 ports + NSE vuln scripts
sudo python3 recon.py -t scanme.nmap.org -i aggressive

# Generate both HTML and PDF report
sudo python3 recon.py -t scanme.nmap.org --format both

# Add Shodan passive enrichment (get free key at shodan.io)
sudo python3 recon.py -t 192.168.1.1 --shodan-key YOUR_API_KEY_HERE

# Fast subnet sweep — skip slow steps
sudo python3 recon.py -t 192.168.1.0/24 -i quick --no-cve --no-subdomains

# View diff between current and last scan
sudo python3 recon.py -t 192.168.1.1 --history
```

### All CLI Flags

| Flag | Description |
|------|-------------|
| `-t` / `--target` | Target IP, domain, or CIDR subnet — **required** |
| `-o` / `--output` | Output filename base (no extension). Default: `netrecon_report` |
| `-i` / `--intensity` | Scan depth: `quick` / `normal` / `aggressive` |
| `--shodan-key KEY` | Shodan API key for passive enrichment |
| `--no-cve` | Skip NVD CVE lookup (faster scans) |
| `--no-subdomains` | Skip subfinder + DNS brute-force |
| `--format` | `html` (default) or `both` (HTML + PDF) |
| `--history` | Show previous scan history and port diff |

---

<div align="center">

## ⚙️ Scan Intensity Levels

</div>

| Level | Nmap Flags Used | Est. Time | Best For |
|-------|----------------|-----------|----------|
| `quick` | `-sV -T4 --open -F` | 20–60 sec | Large subnets, quick overview |
| `normal` | `-sV -sC -O -A --traceroute -T4` | 2–5 min | Standard recon — most situations |
| `aggressive` | `-sV -sC -O -A --traceroute --script=vuln -T4 -p-` | 15–30 min | Full pentest, deep audit |

---

<div align="center">

## 🔧 Troubleshooting

</div>

> Every issue below explains **why** it happens (tied to the actual source code), the **exact command** to fix it, and how to **verify** the fix worked. Run the [Master Health Check](#-master-health-check) first to see everything at once.

---

### ❌ Issue 1 — `ModuleNotFoundError: No module named 'whois'`

**Which file causes this:** `recon.py` line 14 imports `from modules.whois_dns import WhoisDNS`, and `whois_dns.py` uses the `whois` library internally.

**Why it happens:** Kali Linux uses a "externally managed" Python environment. Running plain `pip3 install` without the `--break-system-packages` flag is blocked by the OS, so the package never actually gets installed.

**Fix:**
```bash
# --break-system-packages tells pip it is safe to install
# into Kali's system Python — this is intentional and safe on your own machine
pip3 install python-whois --break-system-packages
```

**Verify it worked:**
```bash
python3 -c "import whois; print('[OK] python-whois is installed')"
```

---

### ❌ Issue 2 — `ModuleNotFoundError: No module named 'dns'`

**Which file causes this:** `whois_dns.py` uses `dnspython` for DNS resolution. The Python import name is `dns`, but the pip package name is `dnspython` — these are different and both must be correct.

**Why it happens:** Same Kali protected-environment issue as above, or the package was installed for a different Python version.

**Fix:**
```bash
pip3 install dnspython --break-system-packages
```

**Verify it worked:**
```bash
python3 -c "import dns.resolver; print('[OK] dnspython is installed')"
```

**Install both at once (recommended):**
```bash
pip3 install python-whois dnspython requests --break-system-packages
```

---

### ❌ Issue 3 — `nmap: command not found` or scan returns 0 hosts

**Which file causes this:** `scanner.py` in the `NmapScanner.scan()` method runs `subprocess.run(["nmap"] + self.flags + [...])`. If nmap is not on PATH, Python raises `FileNotFoundError` — which scanner.py catches and returns `{"error": "nmap not found", "hosts": [], "total_ports": 0}`.

**Why it happens:** nmap is not installed, or you're running as a regular user on a system where nmap is only in root's PATH.

**Fix:**
```bash
sudo apt install nmap -y

# Confirm nmap is now available and check its version
nmap --version
```

**Verify scan works (safe legal test target):**
```bash
sudo python3 recon.py -t scanme.nmap.org -i quick --no-cve --no-subdomains
```

---

### ❌ Issue 4 — OS detection shows "Unknown" / 0% accuracy

**Which file causes this:** `scanner.py` passes the `-O` flag for OS detection in `normal` and `aggressive` modes. Nmap requires raw socket access to send OS probe packets. Without root, nmap silently skips `-O` and the `<os>` element is absent from the XML — so `_parse_xml()` returns `"os": "Unknown"`.

**Why it happens:** You ran the script **without `sudo`**. Nmap needs kernel-level socket access for OS fingerprinting.

**Fix:**
```bash
# Always run recon.py with sudo — nmap needs it for:
# -O (OS detection), -A (aggressive), raw packet crafting
sudo python3 recon.py -t <target> -i normal
```

**Important:** Never run `sudo python3` on a script you didn't write — always review the code first. NetRecon's source is fully readable in the `modules/` folder.

---

### ❌ Issue 5 — CVE lookup returns empty / `{}` results

**Which file causes this:** `cve_lookup.py` in `_query_nvd()` calls `urllib.request.urlopen()` against `https://services.nvd.nist.gov/rest/json/cves/2.0`. The function has a bare `except Exception: return []` — any error (rate limit, timeout, DNS failure) silently returns nothing.

**Why it happens:** Three common causes:
1. **NVD rate limit** — unauthenticated users are limited to ~5 requests per 30 seconds. Scanning a host with many services can exhaust this quickly.
2. **No internet access** — your Kali VM is isolated or uses a proxy.
3. **NVD service downtime** — the NIST API occasionally goes offline.

**Fix A — Wait and retry:**
```bash
# The 0.6s sleep between queries in cve_lookup.py helps,
# but a burst scan with many services can still hit the limit.
# Wait 30 seconds, then re-run:
sudo python3 recon.py -t <target> -i normal
```

**Fix B — Skip CVE lookup entirely:**
```bash
# --no-cve skips all NVD calls — use this for subnet scans or when offline
sudo python3 recon.py -t <target> --no-cve
```

**Fix C — Manually test if NVD API is reachable:**
```bash
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=apache&resultsPerPage=1" | python3 -m json.tool | head -5
# If this prints JSON → NVD is up and reachable from your machine
# If it times out or errors → your network can't reach NVD
```

---

### ❌ Issue 6 — `subfinder: command not found`

**Which file causes this:** `subdomain_enum.py` in `_run_subfinder()` calls `subprocess.run(["subfinder", "-d", domain, "-silent"])`. If subfinder isn't installed, it raises `FileNotFoundError`, which the code catches and silently skips — then falls back to the built-in DNS brute-force wordlist.

**Why it happens:** `subfinder` is a Go binary that isn't pre-installed on all Kali versions.

**Fix A — Install via apt:**
```bash
sudo apt install subfinder -y
subfinder -version   # verify
```

**Fix B — Install via Go (if apt doesn't have it):**
```bash
sudo apt install golang -y
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Make it available system-wide:
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc
subfinder -version
```

**Fix C — Skip subdomain enumeration:**
```bash
# Even without subfinder, the built-in DNS brute-force in subdomain_enum.py
# still checks: www, mail, ftp, admin, dev, staging, api, test,
#               portal, vpn, remote, webmail, smtp, cdn, static,
#               blog, shop, secure, login, app
# Use --no-subdomains only if you want to skip everything:
sudo python3 recon.py -t <target> --no-subdomains
```

---

### ❌ Issue 7 — Topology graph is blank / empty in the HTML report

**Which file causes this:** `report_gen.py` generates an HTML report that loads vis.js from a CDN (`https://unpkg.com/vis-network/...`). If the browser has no internet connection, the `<script>` tag fails to load and the `<canvas>` inside the topology section renders blank.

**Why it happens:** Your browser or VM has no internet access (common in isolated lab environments).

**Fix A — Open in a browser with internet access:**
```bash
firefox output/netrecon_report_*.html
# If Firefox has internet access, the CDN script loads and the graph renders
```

**Fix B — Bundle vis.js locally so reports work offline:**
```bash
# Step 1: Download vis.js once while you have internet
wget https://unpkg.com/vis-network/standalone/umd/vis-network.min.js \
     -O output/vis-network.min.js

# Step 2: In report_gen.py, find the CDN script tag and replace it:
# BEFORE:
#   <script src="https://unpkg.com/vis-network/..."></script>
# AFTER:
#   <script src="vis-network.min.js"></script>
#
# Now copy vis-network.min.js alongside every generated report
```

---

### ❌ Issue 8 — PDF export fails / `wkhtmltopdf: command not found`

**Which file causes this:** `report_gen.py` in `generate_pdf()` calls `wkhtmltopdf` as a subprocess to convert the HTML report to PDF. The `--format both` flag triggers this path.

**Why it happens:** `wkhtmltopdf` is a separate system binary — it's not a Python package and won't be installed by pip. Some Kali versions don't include it by default.

**Fix A — Install via apt:**
```bash
sudo apt install wkhtmltopdf -y
wkhtmltopdf --version   # verify
```

**Fix B — If apt fails (newer Kali / Debian Bookworm):**
```bash
# Download the prebuilt .deb from the official wkhtmltopdf releases:
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
sudo apt --fix-broken install -y   # fix any broken dependencies
wkhtmltopdf --version
```

**Fix C — Use HTML-only mode (skip PDF entirely):**
```bash
# Default mode is already HTML only — just don't pass --format both
sudo python3 recon.py -t <target> -i normal
# Report is saved as output/netrecon_report_TIMESTAMP.html
```

---

### ❌ Issue 9 — Scan is extremely slow or hanging

**Which file causes this:** Three parts of the pipeline contribute to slowness:
- `scanner.py` aggressive mode uses `-p-` (all 65,535 ports) which takes 15–30 min
- `cve_lookup.py` adds a 0.6-second sleep per unique service: many services = many sleeps
- `subdomain_enum.py` runs subfinder (up to 60s timeout) + DNS brute-force

**Fix — Use the fastest possible combination:**
```bash
# quick mode: scans only top 100 ports (nmap -F flag), no OS detection
# --no-cve: skips all NVD API calls
# --no-subdomains: skips subfinder and DNS brute-force entirely
sudo python3 recon.py -t <target> -i quick --no-cve --no-subdomains
```

**Speed comparison table:**

| Combination | Approx Time |
|-------------|-------------|
| `aggressive` (default) | 15–30 min |
| `normal` (default) | 2–5 min |
| `normal --no-cve` | 1–2 min |
| `quick --no-cve --no-subdomains` | 20–60 sec |

---

### ❌ Issue 10 — `PermissionError: [Errno 13] Permission denied` on output/

**Which file causes this:** `history.py` computes `DB_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "netrecon_history.db")` and `report_gen.py` writes HTML/PDF into `output/`. If that directory is owned by root (because you ran `sudo` before), your regular user can't write to it.

**Why it happens:** Running with `sudo` the first time creates `output/` as root-owned. Subsequent runs without sudo — or vice versa — cause permission conflicts.

**Fix:**
```bash
# Create output/ and give your current user full ownership
mkdir -p output
sudo chown -R $USER:$USER output/
chmod 755 output/

# Verify permissions look correct:
ls -la | grep output
# Should show: drwxr-xr-x  ...  YOUR_USERNAME  YOUR_USERNAME  output
```

---

### ❌ Issue 11 — `sqlite3.OperationalError: unable to open database file`

**Which file causes this:** `history.py` uses a path relative to `__file__` (the location of `history.py` itself): `os.path.join(os.path.dirname(__file__), "..", "output", "netrecon_history.db")`. This resolves correctly only when Python loads the file from inside the `modules/` directory — which only works if you run from the project root.

**Why it happens:** You're running `recon.py` from a different directory, e.g. `sudo python3 /home/user/NetRecon/recon.py` from `/tmp`. Python's working directory is `/tmp`, so the relative path breaks.

**Fix:**
```bash
# Always cd into the NetRecon project root first, then run:
cd /home/your-username/NetRecon
sudo python3 recon.py -t <target>

# NOT this — running from a different directory breaks relative paths:
# sudo python3 /home/user/NetRecon/recon.py   ← DON'T do this
```

---

### ❌ Issue 12 — `ImportError: cannot import name 'NmapScanner' from 'modules.scanner'`

**Which file causes this:** `recon.py` imports all 8 modules at the top. Python will only find `modules/` as a package if `modules/__init__.py` exists. Without it, the `modules/` folder is just a directory, not a Python package.

**Why it happens:** `__init__.py` was accidentally deleted, not cloned, or the modules directory structure got corrupted.

**Fix — Check what's inside modules/:**
```bash
ls -la modules/
# You should see ALL of these files:
# __init__.py  scanner.py  whois_dns.py  cve_lookup.py
# shodan_lookup.py  subdomain_enum.py  risk_scorer.py
# history.py  report_gen.py
```

**Fix — Recreate __init__.py if it's missing:**
```bash
# __init__.py can be completely empty — its presence is what makes
# the directory a Python package that can be imported with "from modules.x import Y"
touch modules/__init__.py
```

**Fix — Re-clone if multiple files are missing:**
```bash
cd ..
rm -rf NetRecon
git clone https://github.com/RShasikiran/NetRecon.git
cd NetRecon
sudo bash install.sh
```

---

### ❌ Issue 13 — Shodan returns `"error": "Invalid API key"` or `401`

**Which file causes this:** `shodan_lookup.py` in `lookup()` builds the URL as `f"{self.base}/shodan/host/{ip}?key={self.api_key}"`. If the key is wrong, Shodan's API returns HTTP 401 which `urllib.request.urlopen()` raises as an `HTTPError`, caught and returned as `{"error": "...", "ip": ip}`.

**Why it happens:** Incorrect API key, key copied with trailing spaces, or a free key being used to query a private IP (Shodan only indexes public internet IPs).

**Fix — Get your free key:**
```bash
# 1. Register at: https://account.shodan.io
# 2. Your API key is shown on your account page
# 3. Run with the exact key — no quotes needed in the terminal:
sudo python3 recon.py -t 8.8.8.8 --shodan-key abc123yourkeyhere

# Test your key directly:
curl -s "https://api.shodan.io/api-info?key=YOUR_KEY_HERE"
# Good response: {"scan_credits":100,"usage_limits":...}
# Bad response:  {"error":"Invalid API key"}
```

**Note:** Shodan only has data for publicly routable IP addresses. Using it against `192.168.x.x` or `10.x.x.x` will always return no data.

---

### ❌ Issue 14 — `dig: command not found`

**Which file causes this:** `whois_dns.py` in `_dns()` runs `subprocess.run(["dig", "+short", rtype, target])` for each of the 6 DNS record types (A, AAAA, MX, NS, TXT, SOA) and also for the DMARC TXT check. If `dig` isn't found, the `except Exception` silently returns empty lists for all DNS records.

**Why it happens:** The `dnsutils` package (which contains `dig`) isn't installed.

**Fix:**
```bash
sudo apt install dnsutils -y

# Verify dig works:
dig +short A google.com
# Should print an IP address like 142.250.x.x
```

---

### ❌ Issue 15 — `whois: command not found`

**Which file causes this:** `whois_dns.py` in `_whois()` calls `subprocess.run(["whois", target])`. If the `whois` CLI isn't available, the `except Exception` catches the `FileNotFoundError` and returns `{"error": "...", "registrant": "N/A", "registrar": "N/A"}`.

**Fix:**
```bash
sudo apt install whois -y

# Verify:
whois google.com | head -10
```

---

### ❌ Issue 16 — Report file not found after scan completes

**Which file causes this:** `recon.py` in `main()` builds the output path as `os.path.join("output", f"{args.output}_{timestamp}")` — this is a **relative path** from the current working directory. The `output/` directory must exist before the report can be written.

**Why it happens:** The `output/` folder doesn't exist (install.sh wasn't run, or it was deleted).

**Fix:**
```bash
# Create the output directory manually:
mkdir -p output

# Then re-run your scan — the report will be saved there:
sudo python3 recon.py -t <target>

# List reports:
ls -lh output/*.html
```

---

<div align="center">

## 🩺 Master Health Check

</div>

Run this single command after any setup issue — it tests **every dependency NetRecon needs** and tells you exactly what's missing and how to fix it:

```bash
python3 - << 'EOF'
import subprocess, sys, os

print("\n" + "─"*55)
print("  NetRecon — Full Dependency Health Check")
print("─"*55 + "\n")

all_ok = True

# ── Python packages ──────────────────────────────────────
print("  Python Packages:")
py_packages = [
    ("whois",        "python-whois",  "pip3 install python-whois --break-system-packages"),
    ("dns.resolver", "dnspython",     "pip3 install dnspython --break-system-packages"),
    ("sqlite3",      "sqlite3",       "built-in — should always work"),
    ("requests",     "requests",      "pip3 install requests --break-system-packages"),
]
for mod, label, fix in py_packages:
    try:
        __import__(mod)
        print(f"    \033[92m[✓]\033[0m {label}")
    except ImportError:
        print(f"    \033[91m[✗]\033[0m {label}")
        print(f"        Fix: {fix}")
        all_ok = False

# ── System CLI tools ─────────────────────────────────────
print("\n  System CLI Tools:")
cli_tools = [
    ("nmap",        "Core scanner",           "sudo apt install nmap -y"),
    ("whois",       "WHOIS lookup",           "sudo apt install whois -y"),
    ("dig",         "DNS records",            "sudo apt install dnsutils -y"),
    ("subfinder",   "Subdomain enum",         "sudo apt install subfinder -y  (optional)"),
    ("wkhtmltopdf", "PDF export",             "sudo apt install wkhtmltopdf -y  (optional)"),
]
for tool, role, fix in cli_tools:
    r = subprocess.run(["which", tool], capture_output=True)
    if r.returncode == 0:
        path = r.stdout.decode().strip()
        print(f"    \033[92m[✓]\033[0m {tool:15s} ({role})")
    else:
        optional = "(optional)" in fix
        mark = "\033[93m[!]\033[0m" if optional else "\033[91m[✗]\033[0m"
        print(f"    {mark} {tool:15s} ({role})")
        print(f"        Fix: {fix}")
        if not optional:
            all_ok = False

# ── Directory structure ───────────────────────────────────
print("\n  Directory & File Structure:")
checks = [
    ("output/",            "Output folder for reports"),
    ("modules/__init__.py","Package marker (must exist)"),
    ("modules/scanner.py", "Nmap scan engine"),
    ("modules/whois_dns.py","WHOIS + DNS module"),
    ("modules/cve_lookup.py","CVE lookup module"),
    ("modules/shodan_lookup.py","Shodan module"),
    ("modules/subdomain_enum.py","Subdomain module"),
    ("modules/risk_scorer.py","Risk scoring engine"),
    ("modules/history.py", "SQLite history module"),
    ("modules/report_gen.py","Report generator"),
]
for path, desc in checks:
    exists = os.path.isdir(path) if path.endswith("/") else os.path.isfile(path)
    if exists:
        print(f"    \033[92m[✓]\033[0m {path:35s} {desc}")
    else:
        print(f"    \033[91m[✗]\033[0m {path:35s} MISSING — {desc}")
        all_ok = False

# ── Module imports ────────────────────────────────────────
print("\n  Module Imports:")
modules_to_test = [
    ("modules.scanner",        "NmapScanner"),
    ("modules.whois_dns",      "WhoisDNS"),
    ("modules.cve_lookup",     "CVELookup"),
    ("modules.shodan_lookup",  "ShodanLookup"),
    ("modules.subdomain_enum", "SubdomainEnum"),
    ("modules.risk_scorer",    "RiskScorer"),
    ("modules.history",        "ScanHistory"),
    ("modules.report_gen",     "ReportGenerator"),
]
for mod, cls in modules_to_test:
    try:
        m = __import__(mod, fromlist=[cls])
        getattr(m, cls)
        print(f"    \033[92m[✓]\033[0m {mod}.{cls}")
    except Exception as e:
        print(f"    \033[91m[✗]\033[0m {mod}.{cls} — {e}")
        all_ok = False

# ── Final verdict ─────────────────────────────────────────
print("\n" + "─"*55)
if all_ok:
    print("  \033[92m✓  All checks passed — NetRecon is ready to run!\033[0m")
    print("\n  Try: sudo python3 recon.py -t scanme.nmap.org -i quick")
else:
    print("  \033[91m✗  Some issues found — fix the items marked [✗] above.\033[0m")
    print("  After fixing, re-run this check to confirm.")
print("─"*55 + "\n")
EOF
```

---

<div align="center">

## 🛡️ When to Use NetRecon

</div>

| Situation | Use it? |
|-----------|:-------:|
| CTF — recon the target machine before exploitation | ✅ |
| Home lab VMs — Metasploitable, DVWA, VulnHub boxes | ✅ |
| Auditing your own server or home network | ✅ |
| College cybersecurity lab practicals | ✅ |
| Bug bounty recon on authorized targets | ✅ |
| Demonstrating pentesting skills in an interview | ✅ |
| Scanning someone else's system without permission | ❌ Illegal |
| Web application vulnerability testing | ❌ Use Burp Suite |
| Active exploitation / post-exploitation | ❌ Use Metasploit |

---

<div align="center">

## 📌 Pentest Phases Covered

</div>

```
STANDARD PENETRATION TESTING PHASES
─────────────────────────────────────────────────────────────────

  Phase 1 → PASSIVE RECONNAISSANCE    ✅  NetRecon handles this
            WHOIS (whois_dns.py) · DNS records (whois_dns.py)
            Shodan intel (shodan_lookup.py) · Subdomains (subdomain_enum.py)

  Phase 2 → ACTIVE SCANNING           ✅  NetRecon handles this
            Nmap port scan (scanner.py) · OS detection · Service versions
            CVE mapping (cve_lookup.py) · Risk scoring (risk_scorer.py)

  Phase 3 → Exploitation                   Metasploit / manual (out of scope)

  Phase 4 → Post-Exploitation              Manual techniques (out of scope)

  Phase 5 → REPORTING                  ✅  NetRecon handles this
            HTML report + vis.js topology graph (report_gen.py)
            Optional PDF export · SQLite scan history (history.py)

─────────────────────────────────────────────────────────────────
  NetRecon covers Phase 1 (Passive Recon), Phase 2 (Active Scanning),
  and Phase 5 (Reporting) completely and automatically.
```

---

<div align="center">

## 🔬 Tech Stack

</div>

```
Language         →  Python 3.8+
Main Script      →  recon.py  (argparse CLI, 8-phase orchestration)
─────────────────────────────────────────────────────────
Scanner          →  Nmap with NSE scripts  (scanner.py)
                    Flags: -sV -sC -O -A --traceroute --script=vuln -p-
                    Output: XML parsed with xml.etree.ElementTree

WHOIS            →  System whois command  (whois_dns.py)
                    Parsed with regex for registrar, dates, country, NS

DNS              →  System dig command  (whois_dns.py)
                    Records: A AAAA MX NS TXT SOA + SPF + DMARC check

CVE Database     →  NVD REST API v2.0  (cve_lookup.py)
                    Endpoint: services.nvd.nist.gov/rest/json/cves/2.0
                    Supports: cvssMetricV31, cvssMetricV30, cvssMetricV2

Passive Intel    →  Shodan REST API  (shodan_lookup.py)
                    Endpoint: api.shodan.io/shodan/host/{ip}

Subdomains       →  subfinder binary + built-in DNS brute-force (subdomain_enum.py)
                    Wordlist: www mail ftp admin dev staging api test
                              portal vpn remote webmail smtp cdn blog shop

Risk Engine      →  Custom weighted algorithm  (risk_scorer.py)
                    Score = port weights + (CVSS × 2) + Shodan vuln tags

Database         →  SQLite3  (history.py) — built into Python, no install needed
                    Schema: scans(id, target, timestamp, data JSON)

Topology Graph   →  vis.js  (report_gen.py) — loaded from CDN in HTML report

PDF Export       →  wkhtmltopdf  (report_gen.py) — system binary, apt install

CLI              →  Python argparse  (recon.py)
Platform         →  Kali Linux
```

---

<div align="center">

## 🗓️ Roadmap

</div>

- [ ] Flask web dashboard — run and view scans from a browser instead of CLI
- [ ] Auto-screenshot of HTTP/HTTPS services using headless Chromium
- [ ] Metasploit module suggestions matched to found CVEs
- [ ] Docker container for portable cross-platform deployment
- [ ] Telegram / email alerts when risk score changes between scans
- [ ] Multi-target parallel scanning using Python threading

---

<div align="center">

## ⚠️ Legal Disclaimer

</div>

> This tool is for **authorized security testing, CTF competitions, home labs, and educational use only.**
>
> Only scan systems you own or have **explicit written permission** to test.
>
> Unauthorized network scanning is illegal under the **IT Act 2000 (India)**, **Computer Fraud and Abuse Act (USA)**, and equivalent cybercrime laws worldwide.
>
> The author takes no responsibility for misuse of this tool.
>
> **✅ Always safe to scan:** `scanme.nmap.org` — officially provided by the Nmap project for exactly this purpose.

---

<div align="center">

## 👨‍💻 About

</div>

<div align="center">

Built by **R Shasi Kiran** — BTech Cybersecurity Final Year Capstone Project.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-RShasikiran-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RShasikiran)

<br>

**⭐ Star this repo if it helped you**

<br>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 130" width="100%">
  <defs>
    <linearGradient id="ftbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#010b18"/>
      <stop offset="50%"  stop-color="#051a30"/>
      <stop offset="100%" stop-color="#010b18"/>
    </linearGradient>
    <linearGradient id="ftwave" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#00d4ff" stop-opacity="0"/>
      <stop offset="30%"  stop-color="#00d4ff" stop-opacity="0.45"/>
      <stop offset="70%"  stop-color="#0066ff" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ftwave2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#0044cc" stop-opacity="0"/>
      <stop offset="50%"  stop-color="#00eeff" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0044cc" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="ftcenter" cx="50%" cy="100%" r="60%">
      <stop offset="0%"   stop-color="#00d4ff" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>
    </radialGradient>
    <filter id="ftglow">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="ftgrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#00d4ff" stroke-width="0.12" stroke-opacity="0.14"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="900" height="130" fill="url(#ftbg)"/>
  <rect width="900" height="130" fill="url(#ftgrid)"/>
  <rect width="900" height="130" fill="url(#ftcenter)"/>

  <!-- Wave shapes flowing upward from bottom -->
  <path d="M0,80 C120,55 240,95 360,68 C480,42 600,82 720,58 C810,40 870,72 900,58 L900,0 L0,0 Z"
        fill="#00d4ff" fill-opacity="0.05"/>
  <path d="M0,100 C180,75 360,110 540,85 C690,65 800,100 900,80 L900,0 L0,0 Z"
        fill="#0044aa" fill-opacity="0.07"/>

  <!-- Top border glow line -->
  <rect x="0" y="0" width="900" height="2.5" fill="url(#ftwave)"/>

  <!-- Corner brackets -->
  <g stroke="#00d4ff" stroke-width="1.8" stroke-opacity="0.65" fill="none">
    <polyline points="18,18 18,8 28,8"/>
    <polyline points="872,8 882,8 882,18"/>
    <polyline points="18,112 18,122 28,122"/>
    <polyline points="872,122 882,122 882,112"/>
  </g>

  <!-- Circuit lines left -->
  <g stroke="#00d4ff" stroke-opacity="0.18" stroke-width="0.9" fill="none">
    <polyline points="0,40 60,40 60,55 130,55"/>
    <polyline points="0,75 80,75 80,62 155,62"/>
    <circle cx="60"  cy="40" r="2.5" fill="#00d4ff" opacity="0.5"/>
    <circle cx="80"  cy="75" r="2.5" fill="#00d4ff" opacity="0.5"/>
    <circle cx="130" cy="55" r="2"   fill="#00ffee" opacity="0.6"/>
  </g>

  <!-- Circuit lines right -->
  <g stroke="#00d4ff" stroke-opacity="0.18" stroke-width="0.9" fill="none">
    <polyline points="900,40 840,40 840,55 770,55"/>
    <polyline points="900,75 820,75 820,62 745,62"/>
    <circle cx="840" cy="40" r="2.5" fill="#00d4ff" opacity="0.5"/>
    <circle cx="820" cy="75" r="2.5" fill="#00d4ff" opacity="0.5"/>
    <circle cx="770" cy="55" r="2"   fill="#00ffee" opacity="0.6"/>
  </g>

  <!-- Divider line with diamonds -->
  <line x1="80" y1="65" x2="380" y2="65" stroke="url(#ftwave)" stroke-width="1"/>
  <line x1="520" y1="65" x2="820" y2="65" stroke="url(#ftwave)" stroke-width="1"/>
  <polygon points="450,58 458,65 450,72 442,65" fill="#00d4ff" opacity="0.8" filter="url(#ftglow)"/>

  <!-- NetRecon label -->
  <text x="450" y="62"
        font-family="'Courier New', Courier, monospace"
        font-size="10" fill="#00d4ff"
        text-anchor="middle" letter-spacing="4" opacity="0.9"
        filter="url(#ftglow)">N E T R E C O N</text>

  <!-- Tagline -->
  <text x="450" y="88"
        font-family="'Courier New', Courier, monospace"
        font-size="9.5" fill="#7ecfff"
        text-anchor="middle" letter-spacing="2" opacity="0.7">AUTHORIZED USE ONLY  ·  KALI LINUX  ·  MIT LICENSE</text>

  <!-- Scan dots -->
  <g fill="#00ffaa" opacity="0.7" filter="url(#ftglow)">
    <circle cx="445" cy="102" r="2"/>
    <circle cx="450" cy="102" r="2.5"/>
    <circle cx="455" cy="102" r="2"/>
  </g>
  <g fill="#00d4ff" opacity="0.35">
    <circle cx="435" cy="102" r="1.5"/>
    <circle cx="465" cy="102" r="1.5"/>
    <circle cx="425" cy="102" r="1"/>
    <circle cx="475" cy="102" r="1"/>
  </g>

  <!-- Bottom border -->
  <rect x="0" y="127.5" width="900" height="2.5" fill="url(#ftwave2)"/>
</svg>

</div>
