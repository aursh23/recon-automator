Recon Automator

An automated OSINT reconnaissance tool for the initial recon phase of ethical hacking / penetration testing. Takes a URL or IP address and extracts WHOIS data, DNS records, HTTP headers, SSL certificate info, subdomains, and geolocation/ASN data — all through a simple Flask web interface, with results exportable as a tabulated `.txt` report.

Features
- Accepts either a domain/URL or a raw IP address (auto-resolves the other)
- WHOIS lookup (registrar, creation/expiry dates, nameservers)
- DNS record enumeration (A, AAAA, MX, NS, TXT, CNAME)
- HTTP response header analysis (server, security headers, cookies, redirect chain)
- SSL/TLS certificate inspection (issuer, validity, Subject Alternative Names)
- Subdomain enumeration via certificate transparency data
- IP geolocation, ASN, and CDN/WAF detection
- Web-based GUI (Flask) with downloadable text reports

Tech Stack :
Python · Flask · dnspython · python-whois · requests · tabulate

Setup
```bash
git clone https://github.com/aursh23/recon-automator.git
cd recon-automator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```
Then open `http://localhost:5000` in your browser.

Screenshots
*(add screenshots here)*

Disclaimer
This tool is for **educational purposes and authorized security testing only**. Do not scan or gather information on any system without explicit permission from its owner. Unauthorized reconnaissance may violate computer misuse laws.

Author
Aursh Sharma
