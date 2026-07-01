import requests


def get_subdomains(domain):
    """Query hackertarget.com for subdomains (fallback: crt.sh unreliable)."""
    result = {
        "Subdomains Found": "N/A",
        "Subdomain Count": "0"
    }

    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"

    try:
        response = requests.get(url, timeout=15)

        if response.status_code == 200 and "error" not in response.text.lower() and response.text.strip():
            lines = response.text.strip().split("\n")
            subdomains = set()

            for line in lines:
                parts = line.split(",")
                if parts:
                    subdomains.add(parts[0].strip().lower())

            sorted_subs = sorted(subdomains)
            result["Subdomains Found"] = ", ".join(sorted_subs) if sorted_subs else "None found"
            result["Subdomain Count"] = str(len(sorted_subs))
        else:
            result["Subdomains Found"] = f"No data / API limit reached: {response.text.strip()[:100]}"

    except Exception as e:
        result["Subdomains Found"] = f"Lookup failed: {e}"

    return result


# Quick test when running this file directly
if __name__ == "__main__":
    domain = input("Enter domain: ")
    data = get_subdomains(domain)
    for key, value in data.items():
        print(f"{key}: {value}")
