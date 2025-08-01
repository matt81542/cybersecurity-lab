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
  - `-A` → Aggressive scan (includes OS detection, version detection, traceroute, and default scripts)


### `aggressive_scan.txt`
- **Description**: Full-featured scan with OS detection, version info, script scanning, and traceroute
- **Command Used**:

```bash
nmap -A scanme.nmap.org -oN aggressive_scan.txt

```

# Nmap NSE Vulnerability Scan – Mini Cybersecurity Project

This mini project demonstrates how to perform a vulnerability scan using Nmap and one of its NSE (Nmap Scripting Engine) scripts.

## 🔧 Objective

Use the `vulners` NSE script to scan a target and identify known vulnerabilities based on software version detection.

---

## 🛠️ Tools Used

- **Nmap** (Network Mapper)
- **vulners.nse** script
- **Command line interface**

---

## 🖥️ Example Command

```bash
nmap -sV --script vulners scanme.nmap.org -oN vulners_scan.txt
```

### 🔍 Option 3: Nmap Script Scan (NSE) - Vulnerability Scan

Run a vulnerability scan using Nmap’s built-in vulnerability detection scripts:

```bash
nmap --script vuln scanme.nmap.org -oN output_files/vuln_scan.txt
```
