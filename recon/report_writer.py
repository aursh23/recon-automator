import os
from datetime import datetime
from tabulate import tabulate


def write_report(data, target_name):
    """Write recon results dict to a tabulated .txt file in /reports."""
    os.makedirs("reports", exist_ok=True)

    safe_name = target_name.replace(":", "_").replace("/", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/report_{safe_name}_{timestamp}.txt"

    table_data = [[key, value] for key, value in data.items()]
    table_str = tabulate(table_data, headers=["Field", "Value"], tablefmt="grid")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"RECONNAISSANCE REPORT\n")
        f.write(f"Target: {target_name}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        f.write(table_str)
        f.write("\n")

    return filename


# Quick test when running this file directly
if __name__ == "__main__":
    from recon.aggregator import run_recon

    user_input = input("Enter URL or IP: ")
    print("\nRunning recon...\n")
    data = run_recon(user_input)
    filepath = write_report(data, user_input)
    print(f"Report saved to: {filepath}")
