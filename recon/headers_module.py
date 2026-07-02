import requests


def get_http_headers(domain):
    """Fetch HTTP response headers, status code, and redirect chain."""
    result = {
        "Status Code": "N/A",
        "Server": "N/A",
        "X-Powered-By": "N/A",
        "Content-Type": "N/A",
        "Security Headers": "N/A",
        "Redirect Chain": "N/A",
        "Cookies": "N/A"
    }

    url = f"https://{domain}"

    try:
        response = requests.get(url, timeout=8, allow_redirects=True)
        headers = response.headers

        result["Status Code"] = str(response.status_code)
        result["Server"] = headers.get("Server", "Not disclosed")
        result["X-Powered-By"] = headers.get("X-Powered-By", "Not disclosed")
        result["Content-Type"] = headers.get("Content-Type", "N/A")

        # Check common security headers
        sec_headers = ["Strict-Transport-Security", "Content-Security-Policy",
                       "X-Frame-Options", "X-Content-Type-Options"]
        present = [h for h in sec_headers if h in headers]
        result["Security Headers"] = ", ".join(present) if present else "None found"

        # Redirect chain
        if response.history:
            chain = [r.url for r in response.history] + [response.url]
            result["Redirect Chain"] = " -> ".join(chain)
        else:
            result["Redirect Chain"] = "No redirects"

        # Cookies
        if response.cookies:
            cookie_names = [c.name for c in response.cookies]
            result["Cookies"] = ", ".join(cookie_names)
        else:
            result["Cookies"] = "None"

    except requests.exceptions.RequestException as e:
        result["Status Code"] = f"Request failed: {e}"

    return result



if __name__ == "__main__":
    domain = input("Enter domain: ")
    data = get_http_headers(domain)
    for key, value in data.items():
        print(f"{key}: {value}")
