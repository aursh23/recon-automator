import whois


def get_whois(domain):
    """Fetch WHOIS info for a domain. Returns a dict of key fields."""
    result = {
        "Registrar": "N/A",
        "Domain Created": "N/A",
        "Domain Expires": "N/A",
        "Nameservers": "N/A",
        "Registrant Org": "N/A"
    }

    try:
        w = whois.whois(domain)

        result["Registrar"] = w.registrar or "N/A"

        
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]
        result["Domain Created"] = str(created) if created else "N/A"

        expires = w.expiration_date
        if isinstance(expires, list):
            expires = expires[0]
        result["Domain Expires"] = str(expires) if expires else "N/A"

        if w.name_servers:
            if isinstance(w.name_servers, list):
                result["Nameservers"] = ", ".join(sorted(set(w.name_servers)))
            else:
                result["Nameservers"] = str(w.name_servers)

        result["Registrant Org"] = w.org or "N/A"

    except Exception as e:
        result["Registrar"] = f"WHOIS lookup failed: {e}"

    return result


if __name__ == "__main__":
    domain = input("Enter domain: ")
    data = get_whois(domain)
    for key, value in data.items():
        print(f"{key}: {value}")
