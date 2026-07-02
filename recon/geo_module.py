import requests


def get_geo_info(ip):
    """Fetch geolocation, ASN, org, and CDN hints for an IP."""
    result = {
        "Country": "N/A",
        "Region": "N/A",
        "City": "N/A",
        "ISP/Org": "N/A",
        "ASN": "N/A",
        "Likely CDN/WAF": "N/A"
    }

    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,as"

    try:
        response = requests.get(url, timeout=8)
        data = response.json()

        if data.get("status") == "success":
            result["Country"] = data.get("country", "N/A")
            result["Region"] = data.get("regionName", "N/A")
            result["City"] = data.get("city", "N/A")
            result["ISP/Org"] = data.get("isp", "N/A")
            result["ASN"] = data.get("as", "N/A")

            org_text = (data.get("org", "") + " " + data.get("isp", "")).lower()
            cdn_keywords = ["cloudflare", "akamai", "fastly", "amazon", "google",
                             "microsoft", "azure", "cloudfront"]
            detected = [kw for kw in cdn_keywords if kw in org_text]
            result["Likely CDN/WAF"] = ", ".join(detected).title() if detected else "None detected"
        else:
            result["Country"] = f"Lookup failed: {data.get('message', 'unknown error')}"

    except Exception as e:
        result["Country"] = f"Lookup failed: {e}"

    return result



if __name__ == "__main__":
    ip = input("Enter IP address: ")
    data = get_geo_info(ip)
    for key, value in data.items():
        print(f"{key}: {value}")
