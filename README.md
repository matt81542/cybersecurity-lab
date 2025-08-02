![Tool Added](https://img.shields.io/badge/tool-WHOIS-blue)

# 🛡️ cybersecurity-lab

A collection of cybersecurity practice projects, scripts, and notes. This repository helps document my hands-on learning journey in cybersecurity — from scanning and scripting to log analysis and packet capture.

---

## 📁 Project Structure

| Folder | Contents |
|--------|----------|
| `nmap/` | Sample Nmap scans and outputs |
| `vulns/` | Vulnerability scan write-ups and VM labs |
| `siem/` | SIEM logs and analysis notes |
| `wireshark/` | Packet captures and notes |
| `tools/` | Custom Python tools (network scanner, log parser, etc.) |

---

## 🚀 Projects & Tools

### 🔍 Nmap Scans
- Basic Nmap commands and saved results
- Scripts to parse or filter scan outputs *(coming soon)*

### 🛠️ Python Tools
- `scan_network.py`: Scans a given IP range and prints host/port info
- `port_sweeper.py`: Basic port scan over a range of IPs (WIP)
- More tools coming soon (packet capture, log parser, etc.)

### 🧪 Vulnerability Scanning & VM Labs
- Vulnerability scan write-ups using Nessus, OpenVAS, and manual enumeration
- Hands-on labs with vulnerable VMs like Metasploitable 2 and OWASP Broken Web Apps
- Scan reports stored under respective `scan_reports/` subfolders for transparency and reference

### 📊 SIEM & Logs
- Sample logs
- Manual and automated analysis approaches

### 🌐 Wireshark Captures
- `.pcap` files and explanations of what they reveal
- Notes on protocols, suspicious traffic, etc.

---

🔄 **Tool Maintenance**

I regularly update and improve scripts as I learn more efficient or secure techniques.  
Expect small changes, improved error handling, and additional features over time.

Current focus:
- Making tools modular and reusable
- Logging results to files

---

## Setup

Install required Python packages:  
```bash
pip install -r requirements.txt
