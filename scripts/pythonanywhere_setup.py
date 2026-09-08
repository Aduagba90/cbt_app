#!/usr/bin/env python3
"""
PrepNova CBT — one-command installer / updater for PythonAnywhere.

Run this inside a PythonAnywhere *Bash console*:

    curl -sL https://raw.githubusercontent.com/Aduagba90/cbt_app/main/scripts/pythonanywhere_setup.py -o setup.py && python3 setup.py

First run  → asks 3 questions (admin e-mail, admin password, WhatsApp number), then
             downloads the code, installs packages, writes ~/.prepnova.env, creates the
             website at https://<username>.pythonanywhere.com, forces HTTPS, reloads.
Later runs → "update mode": pulls the latest code from GitHub and reloads the website.
             Students, results, payments and uploaded questions are never touched
             (the live database lives outside the code folder, in ~/prepnova-data/).

Everything it does is idempotent: running it twice is safe.
"""
import getpass
import json
import os
import re
import secrets
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

REPO = "https://github.com/Aduagba90/cbt_app.git"
HOME = os.path.expanduser("~")
CODE = os.path.join(HOME, "cbt_app")
DATA = os.path.join(HOME, "prepnova-data")
ENV_FILE = os.path.join(HOME, ".prepnova.env")
VENV = os.path.join(HOME, ".virtualenvs", "prepnova")
USER = os.environ.get("USER") or getpass.getuser()
DOMAIN = f"{USER.lower()}.pythonanywhere.com"
TOKEN = os.environ.get("API_TOKEN", "")
HOST = "eu.pythonanywhere.com" if "eu.pythonanywhere.com" in os.environ.get("PYTHONANYWHERE_SITE", "") else "www.pythonanywhere.com"
API = f"https://{HOST}/api/v0/user/{USER}"
WSGI = f"/var/www/{USER.lower()}_pythonanywhere_com_wsgi.py"


def say(msg):
    print(f"\n==> {msg}", flush=True)


def die(msg):
    print(f"\n!! {msg}\n", file=sys.stderr)
    sys.exit(1)


def run(cmd, **kw):
    r = subprocess.run(cmd, shell=True, text=True, capture_output=True, **kw)
    if r.returncode != 0:
        die(f"Command failed: {cmd}\n{r.stdout}\n{r.stderr}")
    return r.stdout


def api(method, path, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(f"{API}{path}", data=body, method=method,
                                 headers={"Authorization": f"Token {TOKEN}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode() or "{}"
            return resp.status, (json.loads(raw) if raw.strip().startswith(("{", "[")) else raw)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def check_token():
    if not TOKEN:
        die("No API token found.\n"
            "  Fix: open the 'Account' page → 'API Token' tab → 'Create a new API token',\n"
            "  then CLOSE this console, open a NEW Bash console and run the command again.")


def python_version():
    v = sys.version_info
    return f"{v.major}.{v.minor}"


def ensure_code():
    if os.path.isdir(os.path.join(CODE, ".git")):
        say("Updating code from GitHub")
        run(f"cd {CODE} && git fetch -q origin && git reset -q --hard origin/main")
    else:
        say("Downloading code from GitHub")
        run(f"git clone -q {REPO} {CODE}")


def ensure_venv():
    if not os.path.exists(os.path.join(VENV, "bin", "python")):
        say(f"Creating Python {python_version()} environment (one-time)")
        os.makedirs(os.path.dirname(VENV), exist_ok=True)
        run(f"python{python_version()} -m venv {VENV}")
    say("Installing packages (2–4 minutes the first time)")
    run(f"{VENV}/bin/pip install -q --no-cache-dir -r {CODE}/requirements.txt")


def read_env():
    env = {}
    if os.path.exists(ENV_FILE):
        for line in open(ENV_FILE):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def write_env(env):
    order = ["FLASK_ENV", "SECRET_KEY", "APP_URL", "DATABASE_PATH", "SQLITE_JOURNAL_MODE", "ADMIN_EMAIL", "ADMIN_PASSWORD",
             "SUPPORT_EMAIL", "SUPPORT_WHATSAPP", "SESSION_COOKIE_SECURE", "WAEC_ENABLED",
             "PAYSTACK_PUBLIC_KEY", "PAYSTACK_SECRET_KEY", "MAIL_USERNAME", "MAIL_PASSWORD"]
    keys = order + [k for k in env if k not in order]
    with open(ENV_FILE, "w") as fh:
        fh.write("# PrepNova CBT settings — edit with the Files tab, then reload the website.\n")
        fh.write("# Put comments on their own line; text after a value is read as part of it.\n")
        for k in keys:
            if k in env:
                fh.write(f"{k}={env[k]}\n")
    os.chmod(ENV_FILE, 0o600)


def ask(prompt, default=None, secret=False, validate=None):
    while True:
        shown = f"{prompt}{f' [{default}]' if default else ''}: "
        val = (getpass.getpass(shown) if secret else input(shown)).strip()
        if not val and default:
            val = default
        if validate:
            problem = validate(val)
            if problem:
                print(f"   {problem}")
                continue
        if val:
            return val


def ensure_env():
    env = read_env()
    first = not env
    if first:
        say("A few settings (asked only once)")
        env["ADMIN_EMAIL"] = ask("Admin e-mail (you will log in to /admin_login with this)",
                                 validate=lambda v: None if re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", v) else "That is not an e-mail address.")
        env["ADMIN_PASSWORD"] = ask("Admin password, 10+ characters (typing is hidden)", secret=True,
                                    validate=lambda v: None if len(v) >= 10 and v not in ("admin123", "password") else "Use at least 10 characters, not a default.")
        env["SUPPORT_WHATSAPP"] = ask("Support WhatsApp number, digits only, e.g. 2348012345678",
                                      validate=lambda v: None if re.match(r"^234\d{10}$", v) else "Format: 234 followed by 10 digits (no + or spaces).")
        env["SUPPORT_EMAIL"] = ask("Support e-mail shown to students", default=env["ADMIN_EMAIL"])
    env.setdefault("FLASK_ENV", "production")
    env.setdefault("SECRET_KEY", secrets.token_hex(32))
    env.setdefault("APP_URL", f"https://{DOMAIN}")
    env.setdefault("DATABASE_PATH", os.path.join(DATA, "database.db"))
    env.setdefault("SQLITE_JOURNAL_MODE", "DELETE")
    env.setdefault("SESSION_COOKIE_SECURE", "1")
    env.setdefault("WAEC_ENABLED", "0")
    write_env(env)
    os.makedirs(DATA, exist_ok=True)
    return env, first


def write_wsgi():
    say("Writing the website start file")
    os.makedirs(os.path.dirname(WSGI), exist_ok=True)
    content = f'''# PrepNova CBT — generated by scripts/pythonanywhere_setup.py
import os, sys
CODE = "{CODE}"
if CODE not in sys.path:
    sys.path.insert(0, CODE)
os.chdir(CODE)

# Load settings from ~/.prepnova.env (never stored in the code folder)
with open("{ENV_FILE}") as fh:
    for line in fh:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

from app import app as application  # noqa: E402
'''
    with open(WSGI, "w") as fh:
        fh.write(content)


def ensure_webapp():
    status, apps = api("GET", "/webapps/")
    if status != 200:
        die(f"Could not talk to PythonAnywhere ({status}): {apps}")
    existing = [a for a in apps if a.get("domain_name") == DOMAIN]
    pyver = "python" + python_version().replace(".", "")
    if not existing:
        say(f"Creating the website https://{DOMAIN}")
        status, out = api("POST", "/webapps/", {"domain_name": DOMAIN, "python_version": pyver})
        if status not in (200, 201):
            die(f"Could not create the website ({status}): {out}\n"
                "  If you already have a different website on the Web tab, delete it first (free accounts allow one).")
        time.sleep(2)
    say("Applying website settings (code folder, environment, HTTPS)")
    status, out = api("PATCH", f"/webapps/{DOMAIN}/", {"source_directory": CODE, "virtualenv_path": VENV, "force_https": True})
    if status not in (200, 201):
        die(f"Could not configure the website ({status}): {out}")
    write_wsgi()
    # Static files served directly by the web server (faster, no Python needed)
    status, mappings = api("GET", f"/webapps/{DOMAIN}/static_files/")
    if status == 200 and not any(m.get("url") == "/static/" for m in mappings):
        api("POST", f"/webapps/{DOMAIN}/static_files/", {"url": "/static/", "path": os.path.join(CODE, "static")})


def reload_site():
    say("Reloading the website")
    status, out = api("POST", f"/webapps/{DOMAIN}/reload/", {})
    if status not in (200, 201):
        die(f"Reload failed ({status}): {out}")
    time.sleep(4)
    try:
        with urllib.request.urlopen(f"https://{DOMAIN}/health", timeout=60) as r:
            ok = json.loads(r.read().decode()).get("ok")
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"   (health check did not answer yet: {exc})")
    return ok


def main():
    if "PYTHONANYWHERE_DOMAIN" not in os.environ and "PYTHONANYWHERE_SITE" not in os.environ:
        die("Run this inside a PythonAnywhere Bash console (Consoles tab → Bash).")
    check_token()
    if shutil.which("git") is None:
        die("git is not available in this console.")
    env, first = ensure_env()
    ensure_code()
    ensure_venv()
    ensure_webapp()
    ok = reload_site()

    print("\n" + "=" * 64)
    if ok:
        print(f"  DONE.  Your site is live at:  https://{DOMAIN}")
    else:
        print(f"  Finished, but https://{DOMAIN}/health did not answer yet.")
        print("  Wait one minute and open the address. If it still fails, open the")
        print("  Web tab → 'Error log' and send the last red lines to your developer.")
    if first:
        print(f"  Admin login:  https://{DOMAIN}/admin_login   ({env['ADMIN_EMAIL']})")
        print(f"  Settings file: {ENV_FILE}   (Paystack keys go here later)")
        print(f"  Database:      {env['DATABASE_PATH']}   (back it up from Admin → Backup)")
    else:
        print("  Code updated from GitHub and website reloaded. Data untouched.")
    print("  Free accounts: press the 'Run until 3 months from today' button on the")
    print("  Web tab whenever it appears, or the site is switched off.")
    print("=" * 64 + "\n")


if __name__ == "__main__":
    main()
