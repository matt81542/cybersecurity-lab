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

# 🔎 Nmap NSE Vulnerability Scan – Mini Cybersecurity Project

This mini project demonstrates how to perform two types of vulnerability scans using Nmap and its powerful NSE (Nmap Scripting Engine). These scans go beyond basic port scanning to identify known vulnerabilities on a target system.

---

## 🎯 Objective

Use Nmap to detect vulnerabilities using two approaches:

- ✅ Built-in `vuln` category scripts
- ✅ The external `vulners` script for version-based CVE mapping

---

## 🛠️ Tools Used

- **Nmap** (Network Mapper)
- **NSE Scripts**:
  - `vuln` (built-in)
  - `vulners` (requires version detection)
- **Command Line Interface**

---

## 📘 Example Scans

### ✅ 1. Built-in Vulnerability Scan (Nmap `vuln` Scripts)

```bash
nmap --script vuln scanme.nmap.org -oN output_files/vuln_scan.txt
nmap -sV --script vulners scanme.nmap.org -oN output_files/vulners_scan.txt
```

> ⚠️ Note: The `vuln` scan was partially successful but encountered a known `nsock_loop` error on Windows before all scripts could complete. This is a documented issue with some NSE scripts on Windows systems.
