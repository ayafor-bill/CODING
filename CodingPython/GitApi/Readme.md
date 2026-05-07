# Intent of `gitapi.py`

This script is a simple GitHub API client that searches for popular Python repositories and inspects the returned JSON structure.

It is intended to:

- query GitHub’s repository search endpoint
- request repositories written in Python
- sort results by star count
- print the HTTP response status
- show the top-level keys in the returned JSON response

---

## Detailed line-by-line explanation

```python
import requests
```

- Imports the `requests` library, which makes HTTP requests easy in Python.
- This library is required to call the GitHub API.

```python
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
```

- Defines the API endpoint URL.
- `search/repositories` is GitHub’s endpoint for searching repositories.
- Query parameters:
  - `q=language:python` means “find repositories where the language is Python”
  - `sort=stars` means “order results by star count”

```python
headers = {'Accept' : 'application/vnd.github.v3+json'}
```

- Sets the HTTP `Accept` header to tell GitHub we want the API v3 JSON format.
- This is a best practice for GitHub API requests.

```python
r = requests.get(url, headers=headers)
```

- Sends a GET request to the GitHub search endpoint.
- Passes the `headers` dictionary with the request.
- Stores the response object in `r`.

```python
print(f"Status code: {r.status_code}")
```

- Prints the HTTP status code returned by GitHub.
- Common values:
  - `200` means success
  - `403` means forbidden/rate-limited
  - `422` means invalid request

```python
response_dict = r.json()
```

- Converts the response body from JSON into a Python dictionary.
- The GitHub search API returns JSON with keys like `total_count`, `items`, etc.

```python
print(response_dict.keys())
```

- Prints the keys at the top level of the JSON response.
- This helps you inspect the structure without printing the entire response.

---

## What the code actually does when run

1. Builds a GitHub search URL for Python repos sorted by stars.
2. Sends the request to GitHub.
3. Prints the HTTP response code so you can verify the request succeeded.
4. Parses the response body as JSON.
5. Prints the list of top-level fields returned by GitHub.

---

## Expected output

If the request succeeds, you will typically see:

- `Status code: 200`
- something like `dict_keys(['total_count', 'incomplete_results', 'items'])`

That means:

- the API call worked
- the response contains repository search metadata
- `items` is the list of matched repositories

---
