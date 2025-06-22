# 🔎 Nmap Scan Examples

This folder contains saved Nmap scan results and the commands used to generate them. These examples are useful for reference, analysis, and learning how different scan types work.

---

## 📄 Files & Descriptions

### `basic_scan.txt`
- **Description**: Service version detection scan of `scanme.nmap.org`
- **Command Used**:

```bash
nmap -sV scanme.nmap.org -oN basic_scan.txt

```
- **Scan Type**:
  - `-sV` → Service version detection
  - `-oN` → Normal output format (plain text)


### `aggressive_scan.txt`
- **Description**: Full-featured scan with OS detection, version info, script scanning, and traceroute
- **Command Used**:

```bash
nmap -A scanme.nmap.org -oN aggressive_scan.txt
