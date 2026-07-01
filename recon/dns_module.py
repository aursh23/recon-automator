import dns.resolver


def get_dns_records(domain):
    """Fetch A, AAAA, MX, NS, TXT, CNAME records for a domain."""
    result = {
        "A Records": "N/A",
        "AAAA Records": "N/A",
        "MX Records": "N/A",
        "NS Records": "N/A",
        "TXT Records": "N/A",
        "CNAME Record": "N/A"
    }

    record_types = {
        "A": "A Records",
        "AAAA": "AAAA Records",
        "MX": "MX Records",
        "NS": "NS Records",
        "TXT": "TXT Records",
        "CNAME": "CNAME Record"
    }

    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5

    for rtype, label in record_types.items():
        try:
            answers = resolver.resolve(domain, rtype)
            values = [str(rdata) for rdata in answers]
            result[label] = ", ".join(values)
        except dns.resolver.NoAnswer:
            result[label] = "None"
        except dns.resolver.NXDOMAIN:
            result[label] = "Domain does not exist"
            break
        except Exception as e:
            result[label] = f"Lookup failed: {e}"

    return result


# Quick test when running this file directly
if __name__ == "__main__":
    domain = input("Enter domain: ")
    data = get_dns_records(domain)
    for key, value in data.items():
        print(f"{key}: {value}")
