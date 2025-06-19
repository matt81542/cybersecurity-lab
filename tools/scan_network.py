import nmap
import sys

# Check if subnet/IP is given as argument
if len(sys.argv) != 2:
    print("Usage: python scan_network.py <subnet>")
    print("Example: python scan_network.py 192.168.1.0/24")
    sys.exit(1)

subnet = sys.argv[1]

# Create the Nmap PortScanner object
nm = nmap.PortScanner()

print(f"Scanning network {subnet}...")

# Run a ping scan
nm.scan(hosts=subnet, arguments='-sn')

print("\n✅ Live hosts found:")
for host in nm.all_hosts():
    print(f"- {host}")
