"""
PrepNova daily renewal job — run once a day (e.g. 07:00).

Does four things (all idempotent — safe to run more than once a day):
  1. Emails students whose plan expires in ~3 days ("renew now" link).
  2. Emails students with auto-renewal ON one day before their card is charged.
  3. Charges saved cards for plans expiring tomorrow (auto-renewal).
  4. Sends win-back emails with a 20% code ~7 days after a plan expires.

Setup on PythonAnywhere: Tasks tab -> Set a scheduled task ->
    /home/<your-username>/.virtualenvs/prepnova/bin/python3 /home/<your-username>/cbt_app/scripts/renewals_daily.py
The venv python is required (Flask etc. live there). The script loads
~/.prepnova.env itself, so it sees the same database and keys as the website.
On other hosts: any daily cron entry works (it also falls back to a repo .env).
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)


def _load_env():
    """Load ~/.prepnova.env (PythonAnywhere — same file the website's WSGI start
    file loads) or a repo .env. Values already in the environment win."""
    candidates = [os.path.expanduser("~/.prepnova.env"), os.path.join(REPO, ".env")]
    for path in candidates:
        try:
            with open(path) as fh:
                for line in fh:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        os.environ.setdefault(key.strip(), value.strip())
        except OSError:
            continue
        if os.path.exists(path):
            return


_load_env()
os.chdir(REPO)

from app import run_renewal_day  # noqa: E402
from db import connect  # noqa: E402

if __name__ == "__main__":
    conn = connect()
    try:
        stats = run_renewal_day(conn)
        print(f"renewal job done: {stats}")
    finally:
        conn.close()
