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

