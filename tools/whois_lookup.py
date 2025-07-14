import whois
import sys

def lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"🔍 WHOIS info for {domain}:\n")
        print(w)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python whois_lookup.py <domain>")
    else:
        lookup(sys.argv[1])
