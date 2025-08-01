import subprocess
import datetime

def run_vuln_scan(target):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"vuln_scan_{target}_{timestamp}.txt"

    print(f"Running Nmap vulnerability scan on {target}...")
    with open(output_file, 'w') as out:
        subprocess.run([
            'nmap',
            '-sV',
            '--script', 'vulners',
            target
        ], stdout=out)

    print(f"Scan complete. Results saved to {output_file}")

if __name__ == "__main__":
    target = input("Enter the IP or domain to scan: ")
    run_vuln_scan(target)
