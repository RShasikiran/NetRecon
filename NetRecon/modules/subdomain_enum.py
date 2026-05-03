"""
subdomain_enum.py — Subdomain enumeration module
Uses subfinder (Kali) to discover subdomains, then resolves each to IP
"""

import subprocess
import socket
import re


class SubdomainEnum:
    def enumerate(self, target):
        # Only works for domain targets
        is_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(/\d+)?$", target)
        if is_ip:
            return []

        # Strip any path
        domain = target.split("/")[0]
        subdomains = set()

        # Try subfinder first
        subdomains.update(self._run_subfinder(domain))

        # Fallback: common subdomain brute-force
        if not subdomains:
            subdomains.update(self._bruteforce(domain))

        results = []
        for sub in list(subdomains)[:50]:  # cap at 50
            ip = self._resolve(sub)
            results.append({
                "subdomain": sub,
                "ip": ip,
                "resolved": ip != "Unresolved",
            })

        return results

    def _run_subfinder(self, domain):
        found = set()
        try:
            proc = subprocess.run(
                ["subfinder", "-d", domain, "-silent"],
                capture_output=True, text=True, timeout=60
            )
            for line in proc.stdout.strip().split("\n"):
                line = line.strip()
                if line and domain in line:
                    found.add(line)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        return found

    def _bruteforce(self, domain):
        """Basic wordlist brute-force using DNS"""
        common = [
            "www", "mail", "ftp", "admin", "dev", "staging", "api",
            "test", "portal", "vpn", "remote", "webmail", "smtp",
            "cdn", "static", "blog", "shop", "secure", "login", "app"
        ]
        found = set()
        for word in common:
            sub = f"{word}.{domain}"
            if self._resolve(sub) != "Unresolved":
                found.add(sub)
        return found

    def _resolve(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except Exception:
            return "Unresolved"
