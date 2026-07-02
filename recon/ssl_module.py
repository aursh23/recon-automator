import ssl
import socket
from datetime import datetime


def get_ssl_info(domain, port=443):
    """Connect on port 443 and pull SSL certificate details."""
    result = {
        "SSL Issuer": "N/A",
        "SSL Subject": "N/A",
        "Valid From": "N/A",
        "Valid Until": "N/A",
        "SAN (Subject Alt Names)": "N/A"
    }

    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=8) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                issuer = dict(x[0] for x in cert.get("issuer", []))
                subject = dict(x[0] for x in cert.get("subject", []))

                result["SSL Issuer"] = issuer.get("organizationName", "N/A")
                result["SSL Subject"] = subject.get("commonName", "N/A")
                result["Valid From"] = cert.get("notBefore", "N/A")
                result["Valid Until"] = cert.get("notAfter", "N/A")

                san_list = cert.get("subjectAltName", [])
                if san_list:
                    sans = [entry[1] for entry in san_list]
                    result["SAN (Subject Alt Names)"] = ", ".join(sans)

    except Exception as e:
        result["SSL Issuer"] = f"SSL lookup failed: {e}"

    return result



if __name__ == "__main__":
    domain = input("Enter domain: ")
    data = get_ssl_info(domain)
    for key, value in data.items():
        print(f"{key}: {value}")
