import nmap

def scan_network(ip_range):
    scanner = nmap.PortScanner()
    print(f"Scanning {ip_range}...")
    scanner.scan(hosts=ip_range, arguments='-sS -T4')
    
    for host in scanner.all_hosts():
        print(f"\nHost: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                print(f"Port: {port}\tState: {scanner[host][proto][port]['state']}")

if __name__ == "__main__":
    target_range = input("Enter IP range to scan (e.g., 192.168.1.0/24): ")
    scan_network(target_range)
