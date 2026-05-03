"""
history.py — Scan history & diff engine
Stores scan results in SQLite, diffs against previous scan
"""

import sqlite3
import json
import os
from datetime import datetime


DB_PATH = os.path.join(os.path.dirname(__file__), "..", "output", "netrecon_history.db")


class ScanHistory:
    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH)
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                data TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_and_diff(self, target, results):
        # Get previous scan for this target
        cur = self.conn.execute(
            "SELECT data FROM scans WHERE target=? ORDER BY id DESC LIMIT 1",
            (target,)
        )
        row = cur.fetchone()
        prev = json.loads(row[0]) if row else None

        # Save current scan
        self.conn.execute(
            "INSERT INTO scans (target, timestamp, data) VALUES (?, ?, ?)",
            (target, results["timestamp"], json.dumps(results))
        )
        self.conn.commit()

        if not prev:
            return None

        return self._diff(prev, results)

    def _diff(self, prev, curr):
        prev_ports = self._get_ports(prev)
        curr_ports = self._get_ports(curr)

        new_ports = curr_ports - prev_ports
        closed_ports = prev_ports - curr_ports

        prev_risk = prev.get("risk", {}).get("overall_score", 0)
        curr_risk = curr.get("risk", {}).get("overall_score", 0)

        return {
            "new_ports": len(new_ports),
            "new_ports_list": list(new_ports),
            "closed_ports": len(closed_ports),
            "closed_ports_list": list(closed_ports),
            "risk_delta": curr_risk - prev_risk,
            "prev_timestamp": prev.get("timestamp", "N/A"),
        }

    def _get_ports(self, results):
        ports = set()
        for host in results.get("nmap", {}).get("hosts", []):
            for p in host.get("ports", []):
                ports.add(f"{host.get('ip')}:{p['port']}/{p['protocol']}")
        return ports

    def get_history(self, target, limit=10):
        cur = self.conn.execute(
            "SELECT timestamp, data FROM scans WHERE target=? ORDER BY id DESC LIMIT ?",
            (target, limit)
        )
        rows = cur.fetchall()
        return [{"timestamp": r[0], "risk": json.loads(r[1]).get("risk", {})} for r in rows]
