from recon.input_handler import identify_target, resolve_target
from recon.whois_module import get_whois
from recon.dns_module import get_dns_records
from recon.headers_module import get_http_headers
from recon.ssl_module import get_ssl_info
from recon.subdomain_module import get_subdomains
from recon.geo_module import get_geo_info


def run_recon(raw_input):
    """Run full recon pipeline on a URL or IP. Returns ordered dict of results."""
    report = {}

    identified = identify_target(raw_input)
    resolved = resolve_target(identified)

    report["Target Input"] = raw_input
    report["Target Type"] = identified["type"]
    report["Resolved Domain"] = resolved["domain"] or "N/A"
    report["Resolved IP"] = resolved["ip"] or "N/A"
    report["Reverse Hostname"] = resolved["hostname"] or "N/A"

    domain = resolved["domain"]
    ip = resolved["ip"]

    
    if domain:
        report.update(get_whois(domain))
        report.update(get_dns_records(domain))
        report.update(get_http_headers(domain))
        report.update(get_ssl_info(domain))
        report.update(get_subdomains(domain))
    else:
        report["Note"] = "WHOIS/DNS/HTTP/SSL/Subdomains skipped (raw IP input, no domain)"

   
    if ip and ip != "Could not resolve":
        report.update(get_geo_info(ip))

    return report



if __name__ == "__main__":
    user_input = input("Enter URL or IP: ")
    print("\nRunning recon... this may take 15-30 seconds due to WHOIS/SSL/subdomain lookups.\n")
    data = run_recon(user_input)
    for key, value in data.items():
        print(f"{key}: {value}")
