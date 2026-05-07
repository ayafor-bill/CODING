# What is this?

- This tool was made in an attempt to use leaked databases containing _emails, passwords and links_ to check if the listed credentials were still valid.

__CAUTION: It is free to use however you like but caution is key when using tools like these and empathy is also an emotion to consider if you intend to use this for evil doings(evil doers, please take note).__

## What it does in simple terms

- Most leaks databases contain log in links, emails and passwords in this format _[url|email/login|password]_ or _[url : email/login : password]_.
- The script understands this and attempts to use these credentials.

## How `credstuff.py` Works

### 1. Imports and setup

- `requests`, `urllib3`, and `bs4` are used for HTTP requests and HTML parsing.
- `concurrent.futures` handles parallel execution of credential tests.
- `itertools` is used to cycle through proxies.
- `argparse` handles command-line arguments.
- `logging` and `RotatingFileHandler` save results and warnings to `login_tester.log`.
- `ssl` is configured to disable certificate verification globally (`_create_unverified_context`).
- `urllib3.disable_warnings()` suppresses insecure request warnings.

### 2. Global configuration

- Default field names:
  - `DEFAULT_USERNAME_FIELD = "email"`
  - `DEFAULT_PASSWORD_FIELD = "password"`
  - `CSRF_TOKEN_FIELD = "csrf_token"`
  - `SUCCESS_INDICATOR = "Welcome"`
- A `HEADERS` dictionary defines a fake browser user agent.
- `proxy_cycle` starts as `None` and may be initialized later if proxies are provided.
- `USER_AGENTS` is a list of browser user-agent strings used to randomize requests.

### 3. Helper functions

- `load_proxies(proxy_file)`: reads proxy addresses from a file, one per line.
- `get_next_proxy()`: returns the next proxy from `proxy_cycle`, or `None` if no proxies exist.
- `domain_resolves(url)`: extracts the domain from the URL and confirms it resolves via DNS.
- `is_site_up(url)`: sends a `GET` request and returns `True` if the status code is between 200 and 499.
- `detect_possible_csrf_field(html_text)`: parses HTML and returns the name of a hidden input whose name contains `token`.
- `get_csrf_token(session, url)`: downloads the page, parses hidden input fields, and returns a CSRF token value if found.
- `detect_captcha(response_text)`: checks response text for common CAPTCHA indicators.

### 4. Core test logic: `test_credential(line)`

- The function expects each line in the input file in the format: `url:email:password`.
- It normalizes the line and splits it into:
  - `url`
  - `email`
  - `password`
- If the format is invalid, it returns a skip message.
- It ensures the URL starts with `https://`.
- It checks:
  - DNS resolution of the domain
  - whether the site is reachable
- It creates a `requests.Session()` and randomizes the `User-Agent` header.
- It optionally applies a proxy from `proxy_cycle`.
- It detects whether the URL looks like a JSON API login endpoint:
  - if URL ends with `/api/login`
  - or if it contains `/api/`
- For non-API targets, it attempts to fetch a CSRF token from the login page.
- It builds and sends the login request:
  - JSON payload for API endpoints
  - form data (`data=`) for standard HTML login endpoints
- It analyzes the response:
  - detects CAPTCHA content
  - if status code is `200`, it tries to parse JSON and look for `success` or `authenticated`
  - if JSON parsing fails, it falls back to searching for `SUCCESS_INDICATOR` text in the response
- It returns one of:
  - `[SUCCESS]`
  - `[FAIL]`
  - `[CAPTCHA]`
  - `[PROXY ERROR]`
  - `[ERROR]`
  - `[SKIP]`

### 5. Main execution: `main(file_path, max_workers=10, proxy_file=None)`

- If a proxy file is provided, it loads proxies and creates `proxy_cycle`.
- It reads all input lines from the given credential file.
- It uses a `ThreadPoolExecutor` with `max_workers` threads to execute `test_credential` concurrently.
- It prints and logs each result.

### 6. Command-line behavior

When run as a script:

- `argparse` defines required and optional CLI arguments:
  - positional `file`
  - `--workers`
  - `--proxy-file`
  - `--username-field`
  - `--password-field`
  - `--csrf-field`
  - `--success-indicator`
- CLI argument values override the default global settings.
- Finally, it calls `main()` with the provided file, worker count, and proxy file.

### 7. Overall flow

1. User runs `credstuff.py` with a credentials file and optional proxy file.
2. Script loads configuration and proxies.
3. Each credential line is validated and tested in parallel.
4. Each test:
   - validates the URL,
   - optionally fetches CSRF,
   - sends a login request,
   - checks for success or failure.
5. Results are printed and written to `login_tester.log`.

This script is designed to test credential combinations against login endpoints while supporting proxies, CSRF detection, CAPTCHA detection, and both HTML form and JSON API login flows.
