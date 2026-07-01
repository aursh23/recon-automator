import re
import socket


def clean_input(raw_input):
    """Strip protocol, path, and whitespace from user input."""
    target = raw_input.strip()
    target = re.sub(r'^https?://', '', target)
    target = target.split('/')[0]
    return target


def is_ip_address(target):
    """Check if the string is a valid IPv4 address."""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return bool(re.match(pattern, target))


def identify_target(raw_input):
    """Clean input and return dict with type + cleaned value."""
    target = clean_input(raw_input)
    if is_ip_address(target):
        return {"type": "ip", "value": target}
    else:
        return {"type": "domain", "value": target}


def resolve_target(identified):
    """Given identify_target() output, resolve IP <-> hostname."""
    result = {
        "domain": None,
        "ip": None,
        "hostname": None
    }

    if identified["type"] == "domain":
        result["domain"] = identified["value"]
        try:
            result["ip"] = socket.gethostbyname(identified["value"])
        except socket.gaierror:
            result["ip"] = "Could not resolve"

    elif identified["type"] == "ip":
        result["ip"] = identified["value"]
        try:
            hostname, _, _ = socket.gethostbyaddr(identified["value"])
            result["hostname"] = hostname
        except socket.herror:
            result["hostname"] = "No reverse DNS found"

    return result


# Quick test when running this file directly
if __name__ == "__main__":
    user_input = input("Enter URL or IP: ")
    identified = identify_target(user_input)
    resolved = resolve_target(identified)
    print("Identified:", identified)
    print("Resolved:", resolved)
