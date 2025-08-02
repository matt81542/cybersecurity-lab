# 🔍 Nessus Scan Reports – OWASP Broken Web Apps

This folder contains output files and summaries from **Nessus vulnerability scans** performed against the intentionally vulnerable **OWASP Broken Web Apps** virtual machine.

---

## 📄 Included Files

| File Name                            | Description                              |
|-------------------------------------|------------------------------------------|
| `Basic Scan - Owasp BWA_0q5sll.html` | Full Nessus HTML report – Basic scan     |
| `owasp_bwa_basic_scan.md`           | Summary of results from the basic scan   |
| `owasp bwa scan_oi2kyw.html`        | Full Nessus HTML report – Advanced scan  |

> 📎 **Note**: GitHub doesn’t render `.html` files directly.  
> To view, download and open them in a web browser.

---

## 🧪 Scan Environment

| Setting            | Details                          |
|--------------------|----------------------------------|
| **Tool**           | Tenable Nessus Essentials        |
| **Target**         | OWASP Broken Web Apps VM         |
| **IP Address**     | `192.168.56.101`                 |
| **Hypervisor**     | VirtualBox (Host-only adapter)   |
| **Scan Types**     | Basic Network Scan, Advanced Scan |
| **Output Format**  | HTML + Markdown summary          |
| **Date**           | August 2025                      |

---

## 🔹 Basic Scan – Summary

The **Basic Scan** was conducted using the default Nessus “Basic Network Scan” template. Its purpose was to identify open ports and host-level vulnerabilities without deep credentialed or web application testing.

### 📌 Key Findings

- **Open Ports Detected**:
  - `21` (FTP), `22` (SSH), `25` (SMTP), `80` (HTTP), `139/445` (SMB), `3306` (MySQL), `8080` (HTTP-alt), and others.

- **Critical Issues**:
  - End-of-life operating system: Ubuntu 10.04
  - SSLv2 and SSLv3 still enabled
  - SMB signing not required (risk of MITM)
  - SWEET32 vulnerability due to 64-bit block cipher support

- **High Severity**:
  - Deprecated/weak cryptographic algorithms
  - Badlock vulnerability in Samba
  - Open MySQL server (remote connections allowed)

- **Medium Severity**:
  - Support for TLS 1.0 / 1.1
  - OS and server version disclosure via banners
  - Self-signed SSL certificates
  - SSH configuration allows weak algorithms

- **Low Severity**:
  - ICMP timestamp response enabled
  - Public SSH host key too small
  - General host information disclosures

The scan confirmed that the VM hosts multiple services with outdated configurations, making it highly vulnerable in a real-world scenario. These findings reinforce the need for secure configurations and proper hardening, especially around legacy protocols and services.

📂 **Report File**:  
Open the following file locally in a browser to view full plugin output:

📁 **[Basic Scan Report (HTML)](Basic%20Scan%20-%20Owasp%20BWA_0q5sll.html)**

---

## 🔸 Advanced Scan – Summary

The **Advanced Scan** was conducted using a more thorough Nessus template with web application plugins enabled. The report reveals a large number of vulnerabilities across different severity levels and includes information disclosure, outdated versions, cryptographic weaknesses, and actual exploitable flaws in the hosted web applications.

### 📊 Vulnerability Count

| Severity     | Count |
|--------------|-------|
| 🔴 Critical  | 4     |
| 🟠 High      | 8     |
| 🟡 Medium    | 34    |
| 🔵 Low       | 13    |

### 🚨 Notable Vulnerabilities

- **Apache HTTPD 2.2.14** is outdated and contains multiple known CVEs
- **Apache mod_negotiation Local Source Disclosure** vulnerability
- Multiple pages disclose the OS version (Ubuntu 10.04.4 LTS)
- SSL/TLS vulnerabilities:
  - SSL Medium Strength Cipher Suites Supported (SWEET32)
  - SSL Certificate Signed Using Weak Hashing Algorithm
  - TLS Version 1.0 and 1.1 Protocol Detection
- **phpMyAdmin 3.3.7** vulnerable to SQL Injection (CVE-2010-3055)
- **phpBB** forum is running a vulnerable version with XSS and CSRF issues
- Numerous pages leak server information in headers
- **WebDAV** is enabled and allows unauthenticated access
- jQuery library is outdated and contains known XSS vulnerabilities

These vulnerabilities highlight a range of common misconfigurations and outdated components typically targeted in real-world attacks.

📂 **Report File**:  
Open the following file locally in a browser to view full plugin output:

📁 **[Advanced Scan Report (HTML)](owasp%20bwa%20scan_oi2kyw.html)**
---

## 💡 Notes

- These scans were performed in a **controlled lab environment** for learning and demonstration purposes only.
- The OWASP BWA VM is intentionally vulnerable and designed to simulate real-world attack surfaces for testing and training.
- Reports in this folder support a broader cybersecurity learning project, including vulnerability identification, tool usage, and documentation best practices.
