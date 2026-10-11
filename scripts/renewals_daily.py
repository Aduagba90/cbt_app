"""
PrepNova daily renewal job — run once a day (e.g. 07:00).

Does four things (all idempotent — safe to run more than once a day):
  1. Emails students whose plan expires in ~3 days ("renew now" link).
  2. Emails students with auto-renewal ON one day before their card is charged.
  3. Charges saved cards for plans expiring tomorrow (auto-renewal).
  4. Sends win-back emails with a 20% code ~7 days after a plan expires.

Setup on PythonAnywhere: Tasks tab -> Set a scheduled task ->
    python3 /home/<your-username>/PrepNova-CBT/scripts/renewals_daily.py
(adjust the path to wherever the repo lives; run it from the repo root or set
 PYTHONPATH). On other hosts: any daily cron entry works.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import run_renewal_day  # noqa: E402
from db import connect  # noqa: E402

if __name__ == "__main__":
    conn = connect()
    try:
        stats = run_renewal_day(conn)
        print(f"renewal job done: {stats}")
    finally:
        conn.close()
