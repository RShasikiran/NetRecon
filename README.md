[🌐 View Project Page](https://rshasikiran.github.io/NetRecon/)
 
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:020810,30:0a1628,70:0a3d62,100:00d4ff&height=220&section=header&text=NetRecon&fontSize=90&fontColor=00d4ff&fontAlignY=40&desc=Advanced%20Network%20Reconnaissance%20%26%20Visual%20Reporting%20Tool&descSize=16&descAlignY=62&descColor=7ab4ff&animation=fadeIn&fontAlignX=50"/>

</div>

<div align="center">

```
 ███╗   ██╗███████╗████████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
 ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
 ██╔██╗ ██║█████╗     ██║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
 ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
 ██║ ╚████║███████╗   ██║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
```

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

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,40:0a3d62,100:020810&height=140&section=footer"/>

</div>
