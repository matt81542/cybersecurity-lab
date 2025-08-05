# Rapid7 Nexpose Community Edition - VM Vulnerability Scanning

## Overview

This folder contains resources related to vulnerability scanning using **Rapid7 Nexpose Community Edition** — a free, user-friendly vulnerability scanner with a rich web interface.

Nexpose provides detailed vulnerability assessment reports, helping identify security weaknesses on target systems. This example focuses on scanning a virtual machine (VM) in a lab environment.

---

## Getting Started

### 1. Download and Install Nexpose Community Edition

- Download the Windows installer from Rapid7’s official page:  
  https://www.rapid7.com/products/nexpose/download/  

- Choose **Community Edition** (free, limited to scanning up to 32 IP addresses).

- Run the installer and follow prompts.

- After installation, the web console opens at:  
  `https://localhost:3780`

---

### 2. Configure Your Scan

- Log in with default credentials (`admin` / initial password set on install).

- Navigate to **Sites** > **Create Site**.

- Add your target VM’s IP address (ensure network connectivity and firewall allow scans).

- Save the site and launch a scan.

---

### 3. Review Scan Results

- View scan progress and detailed vulnerability findings in the web console.

- Use interactive dashboards and filters to explore vulnerabilities by severity, CVE, or asset.

---

### 4. Export and Use Reports

- Export scan reports in formats like PDF, CSV, or HTML.

- Save reports in this folder (`reports/`) for documentation and portfolio inclusion.

---

## Example Scan Setup

- Target VM: Metasploitable 2 (IP: `192.168.56.101`)  
- Scan type: Full Network Scan (default policies)  
- Scan duration: Approx. 10-20 minutes depending on VM and network speed

---

## Tips for Effective Use

- Ensure your VM network adapter is configured to allow host machine access (e.g., Host-Only or Bridged mode).

- Update Nexpose regularly to keep vulnerability checks current.

- Review false positives and tune scan policies as needed.

---

## References

- [Rapid7 Nexpose Documentation](https://docs.rapid7.com/nexpose/)  
- [Community Edition Limitations](https://www.rapid7.com/products/nexpose/pricing/)  

---

## Project Notes

This folder supports a portfolio project demonstrating vulnerability scanning skills using a modern, visual tool. Screenshots and reports are included to showcase real-world application.

---

*Created by [Your Name], [Date]*  
