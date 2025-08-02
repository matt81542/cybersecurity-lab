# Nessus Advanced Scan Output – OWASP Broken Web Apps VM

This folder contains the HTML output file from a Nessus Advanced Scan performed against the OWASP Broken Web Apps virtual machine.

## 📄 Included File

- `owasp bwa scan_oi2kyw.html` – Full scan report (open in a web browser)

> ⚠️ GitHub does not render `.html` reports in-browser. To view the file:
> - Download it to your machine
> - Open it locally in your preferred browser

## 🔍 Scan Context

- **Tool**: Tenable Nessus Essentials
- **Scan Template**: Advanced Scan
- **Target**: 192.168.56.101 (Host-only adapter)
- **Duration**: Approx. 1 hour+
- **VM**: OWASP Broken Web Apps
- **Output Location**: This directory

## 📌 Notes

- This output corresponds to the documented process in `vulns/owasp_bwa/nessus_scan_advanced/README.md`.
- The scan includes detection of web application vulnerabilities, obsolete software, and network-level misconfigurations.

# Nessus Advanced Scan - OWASP Broken Web Apps VM

This document outlines the results of an **Advanced Vulnerability Scan** run with Tenable Nessus against the OWASP Broken Web Apps VM.

## 🔍 Scan Overview

- **Scanner**: Tenable Nessus Essentials
- **Scan Template**: Advanced Scan
- **Target**: 192.168.56.101
- **Network Setup**: Host-only network (VirtualBox), IP manually configured
- **Scan Duration**: ~1 hour+
- **Nessus Version**: [Your Nessus version]
- **VM Distro**: OWASP BWA

## 📊 Vulnerability Summary

| Severity     | Count |
|--------------|-------|
| **Critical** | 4     |
| **High**     | 8     |
| **Medium**   | 34    |
| **Low**      | 13    |

## 🚨 Critical Vulnerabilities (CVSS 9.8–10)

- **SSL Version 2 and 3 Protocol Detection** – Obsolete protocols in use.
- **phpBB viewtopic.php SQL Injection**
- **phpMyAdmin < 4.8.6 SQL Injection (PMASA-2019-3)**
- **Canonical Ubuntu Linux End-of-Life (10.04.x)** – No longer supported or patched.

## ⚠️ Notable High/Medium Findings

- **Samba Badlock Vulnerability**
- **SSL Weak Cipher Suites (SWEET32, RC4)**
- **TLS 1.0/SSLv3 Support**
- **Multiple phpBB SQLi and XSS vulnerabilities**
- **SMB Signing not required**
- **JQuery & Apache version disclosure**
- **Clickjacking potential**

## 📁 Report Location

The full HTML report is included in this folder:

📄 [`metatest_ol6d3n.html`](./metatest_ol6d3n.html)

To view it, open the file in your browser.

> _Note: GitHub doesn't render standalone `.html` files in-browser. Download and open locally._

## 📌 Notes

- The OWASP VM had to be configured with a static IP on the Host-only adapter.
- Ping and Nmap were confirmed working before the scan.
- The advanced scan includes web application tests which increase duration.

# 🔍 OWASP Broken Web Apps — Basic Vulnerability Scan

**Scan Type:** Basic scan using Nessus  
**Target:** OWASP BWA VM  
**Date:** [Insert date here]

---

## 🧾 Summary

A basic vulnerability scan was performed against the OWASP BWA virtual machine using Nessus. The target exposed several open ports and services with outdated configurations and known vulnerabilities. Many of these issues are intentional, as OWASP BWA is designed for safe testing and training.

---

## 🔓 Open Ports and Services

- **22/tcp** — OpenSSH  
- **25/tcp** — Postfix SMTP  
- **80/tcp** — Apache HTTP Server  
- **139, 445/tcp** — Samba (SMBv1 enabled)  
- **3306/tcp** — MySQL  
- **8080/tcp** — Apache Tomcat  
- **Others** — Additional services used by vulnerable apps

---

## ⚠️ Vulnerability Summary

| Severity | Count | Examples |
|----------|-------|----------|
| 🔴 Critical | 2 | SSLv2/v3 Support, Unsupported OS (Ubuntu SEoL) |
| 🟠 High | 2 | SWEET32, Samba Badlock |
| 🟡 Medium | 13 | Self-signed certs, outdated jQuery, TLS 1.0, weak hashing |
| 🔵 Low | 5+ | POODLE, ICMP timestamp, weak SSH algorithms |

---

## 📌 Notable Findings

- **SSL/TLS Issues:**  
  - SSLv2, SSLv3, and TLS 1.0 are supported  
  - Self-signed and untrusted certificates  
  - Weak ciphers (RC4, 3DES), weak hashes (SHA-1), and outdated protocols  

- **Outdated Software:**  
  - OS is marked End of Life (Ubuntu 10.04.x)  
  - Apache and Tomcat default files accessible  
  - jQuery vulnerable to XSS (< v3.5.0)

- **Samba Vulnerabilities:**  
  - Badlock CVE present  
  - SMB signing not required (allows MITM attacks)

- **Information Disclosure:**  
  - Apache ETag header leakage  
  - HTTP TRACE enabled  
  - SSH and ICMP configurations allow fingerprinting

---

## 📁 Files Included

- `owasp_bwa_basic_scan.md` — this summary  
- `owasp_bwa_basic_scan.html` — full HTML report exported from Nessus

---

## 💡 Notes

- This VM is purposefully vulnerable for learning and testing.  
- Many of these issues should never be present on production systems.  
- Use this environment to practise detection, reporting, and patching.

