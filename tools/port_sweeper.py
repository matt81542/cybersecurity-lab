import socket

def sweep_ports(target_ip, ports):
    print(f"\nSweeping ports on {target_ip}...\n")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is closed")

if __name__ == "__main__":
    target = input("Enter target IP (e.g., 192.168.1.1): ")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 8080]
    sweep_ports(target, common_ports)
