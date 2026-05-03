#!/usr/bin/env python3
"""
NetRecon - Advanced Network Reconnaissance & Reporting Tool
Author: [Your Name] | BTech Cybersecurity Capstone Project
"""

import argparse
import sys
import os
import json
import time
import subprocess
from datetime import datetime

from modules.scanner import NmapScanner
from modules.whois_dns import WhoisDNS
from modules.cve_lookup import CVELookup
from modules.shodan_lookup import ShodanLookup
from modules.subdomain_enum import SubdomainEnum
from modules.risk_scorer import RiskScorer
from modules.history import ScanHistory
from modules.report_gen import ReportGenerator

BANNER = """
\033[92m
 ███╗   ██╗███████╗████████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
 ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
 ██╔██╗ ██║█████╗     ██║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
 ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
 ██║ ╚████║███████╗   ██║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
\033[0m
\033[90m  Advanced Network Reconnaissance & Reporting Tool v1.0\033[0m
\033[90m  BTech Cybersecurity Capstone Project\033[0m
\033[91m  [!] For authorized use only. Always obtain proper permission.\033[0m
"""

def parse_args():
    parser = argparse.ArgumentParser(
        description="NetRecon — Full-spectrum network recon & reporting tool",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-t", "--target", required=True,
        help="Target IP, hostname, or CIDR range (e.g. 192.168.1.1 or 192.168.1.0/24)")
    parser.add_argument("-o", "--output", default="netrecon_report",
        help="Output filename (without extension). Default: netrecon_report")
    parser.add_argument("-i", "--intensity", choices=["quick", "normal", "aggressive"],
        default="normal", help="Scan intensity level (default: normal)")
    parser.add_argument("--shodan-key", default=None,
        help="Shodan API key for passive enrichment")
    parser.add_argument("--no-cve", action="store_true",
        help="Skip CVE lookup (faster)")
    parser.add_argument("--no-subdomains", action="store_true",
        help="Skip subdomain enumeration")
    parser.add_argument("--format", choices=["html", "both"], default="html",
        help="Output format: html or both (html + pdf). Default: html")
    parser.add_argument("--history", action="store_true",
        help="Show scan history for target and diff with last scan")
    return parser.parse_args()


def print_status(msg, status="*"):
    colors = {"*": "\033[94m", "+": "\033[92m", "!": "\033[91m", "-": "\033[90m"}
    c = colors.get(status, "\033[0m")
    print(f"  {c}[{status}]\033[0m {msg}")


def main():
    print(BANNER)
    args = parse_args()
    target = args.target
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results = {"target": target, "timestamp": timestamp, "scan_intensity": args.intensity}

    print_status(f"Target: \033[93m{target}\033[0m")
    print_status(f"Intensity: {args.intensity} | Format: {args.format}")
    print_status(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Phase 1: Nmap Scan
    print_status("Running nmap scan...", "*")
    scanner = NmapScanner(intensity=args.intensity)
    nmap_data = scanner.scan(target)
    results["nmap"] = nmap_data
    print_status(f"Discovered {len(nmap_data.get('hosts', []))} host(s), {nmap_data.get('total_ports', 0)} open port(s)", "+")

    # Phase 2: WHOIS + DNS
    print_status("Fetching WHOIS & DNS records...", "*")
    whois_dns = WhoisDNS()
    whois_data = whois_dns.lookup(target)
    results["whois_dns"] = whois_data
    print_status("WHOIS & DNS enrichment complete", "+")

    # Phase 3: Shodan
    if args.shodan_key:
        print_status("Querying Shodan...", "*")
        shodan = ShodanLookup(api_key=args.shodan_key)
        shodan_data = shodan.lookup(target)
        results["shodan"] = shodan_data
        print_status("Shodan enrichment complete", "+")
    else:
        results["shodan"] = None
        print_status("Shodan skipped (no API key provided)", "-")

    # Phase 4: CVE Lookup
    if not args.no_cve:
        print_status("Looking up CVEs via NVD API...", "*")
        cve = CVELookup()
        cve_data = cve.lookup_from_nmap(nmap_data)
        results["cves"] = cve_data
        total_cves = sum(len(v) for v in cve_data.values())
        print_status(f"Found {total_cves} CVE(s) across all services", "+")
    else:
        results["cves"] = {}
        print_status("CVE lookup skipped", "-")

    # Phase 5: Subdomain Enumeration
    if not args.no_subdomains:
        print_status("Enumerating subdomains...", "*")
        sub_enum = SubdomainEnum()
        subdomain_data = sub_enum.enumerate(target)
        results["subdomains"] = subdomain_data
        print_status(f"Found {len(subdomain_data)} subdomain(s)", "+")
    else:
        results["subdomains"] = []
        print_status("Subdomain enumeration skipped", "-")

    # Phase 6: Risk Scoring
    print_status("Calculating risk scores...", "*")
    scorer = RiskScorer()
    risk_data = scorer.score(nmap_data, results.get("cves", {}), results.get("shodan"))
    results["risk"] = risk_data
    print_status(f"Overall risk: \033[91m{risk_data.get('overall_label', 'UNKNOWN')}\033[0m", "+")

    # Phase 7: Save to history & diff
    print_status("Saving to scan history...", "*")
    history = ScanHistory()
    diff = history.save_and_diff(target, results)
    results["diff"] = diff
    if diff:
        print_status(f"Diff: {diff.get('new_ports', 0)} new port(s), {diff.get('closed_ports', 0)} closed port(s) since last scan", "+")

    # Phase 8: Generate Report
    print_status("Generating report...", "*")
    reporter = ReportGenerator()
    output_path = os.path.join("output", f"{args.output}_{timestamp}")
    html_path = reporter.generate_html(results, output_path)
    print_status(f"HTML report saved: \033[93m{html_path}\033[0m", "+")

    if args.format == "both":
        pdf_path = reporter.generate_pdf(html_path)
        print_status(f"PDF report saved: \033[93m{pdf_path}\033[0m", "+")

    print()
    print_status("Scan complete!", "+")
    print_status(f"Report: {html_path}", "+")
    print()


if __name__ == "__main__":
    main()
