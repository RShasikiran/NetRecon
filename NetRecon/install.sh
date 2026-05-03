#!/bin/bash
# ─────────────────────────────────────────────────
#  NetRecon — Kali Linux Setup Script
#  Run this once before using recon.py
# ─────────────────────────────────────────────────

RED='\033[0;31m'
GRN='\033[0;32m'
BLU='\033[0;34m'
YEL='\033[1;33m'
NC='\033[0m'

ok()   { echo -e "  ${GRN}[✓]${NC} $1"; }
info() { echo -e "  ${BLU}[*]${NC} $1"; }
warn() { echo -e "  ${YEL}[!]${NC} $1"; }
fail() { echo -e "  ${RED}[✗]${NC} $1"; }

echo ""
echo -e "${BLU} ███╗   ██╗███████╗████████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗${NC}"
echo -e "${BLU} NetRecon — Kali Linux Installer${NC}"
echo ""

# ── Check running as root ──────────────────────────────────────────────────
if [ "$EUID" -ne 0 ]; then
  warn "Not running as root. Some apt installs may fail."
  warn "Run with: sudo bash install.sh"
  echo ""
fi

# ── System tools via apt ───────────────────────────────────────────────────
info "Installing system tools via apt..."
apt-get update -qq 2>/dev/null

for pkg in nmap whois dnsutils subfinder wkhtmltopdf; do
  if dpkg -s "$pkg" &>/dev/null; then
    ok "$pkg already installed"
  else
    info "Installing $pkg..."
    apt-get install -y -qq "$pkg" 2>/dev/null && ok "$pkg installed" || warn "$pkg install failed (optional)"
  fi
done

# ── Python packages ────────────────────────────────────────────────────────
info "Installing Python packages..."
pip3 install python-whois dnspython --break-system-packages -q 2>/dev/null
if python3 -c "import whois, dns" 2>/dev/null; then
  ok "Python packages installed (python-whois, dnspython)"
else
  fail "Python package install failed — try: pip3 install python-whois dnspython --break-system-packages"
fi

# ── Create output dir ──────────────────────────────────────────────────────
mkdir -p output
ok "output/ directory ready"

# ── Make recon.py executable ───────────────────────────────────────────────
chmod +x recon.py
ok "recon.py is executable"

# ── Final check ───────────────────────────────────────────────────────────
echo ""
info "Running dependency check..."
python3 - <<'EOF'
checks = {
    "nmap (CLI)":      ("nmap", None),
    "whois (CLI)":     ("whois", None),
    "dig (DNS utils)": ("dig", None),
    "python-whois":    (None, "whois"),
    "dnspython":       (None, "dns"),
    "sqlite3":         (None, "sqlite3"),
}
import subprocess, sys
all_ok = True
for name, (cli, mod) in checks.items():
    if cli:
        r = subprocess.run(["which", cli], capture_output=True)
        ok = r.returncode == 0
    else:
        try: __import__(mod); ok = True
        except: ok = False
    sym = "✓" if ok else "✗"
    col = "\033[92m" if ok else "\033[91m"
    print(f"  {col}[{sym}]\033[0m {name}")
    if not ok: all_ok = False

print()
if all_ok:
    print("  \033[92m[✓] All dependencies satisfied. Ready to run!\033[0m")
else:
    print("  \033[93m[!] Some optional deps missing — core features will still work.\033[0m")
EOF

echo ""
echo -e "${GRN}─────────────────────────────────────────────────${NC}"
echo -e "${GRN}  Setup complete! Run NetRecon with:${NC}"
echo -e ""
echo -e "  ${YEL}python3 recon.py -t scanme.nmap.org -i normal${NC}"
echo -e ""
echo -e "  ${BLU}# Or for full aggressive scan:${NC}"
echo -e "  ${YEL}python3 recon.py -t <target> -i aggressive --format both${NC}"
echo -e "${GRN}─────────────────────────────────────────────────${NC}"
echo ""
