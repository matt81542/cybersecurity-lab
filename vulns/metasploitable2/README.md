# Metasploitable 2 Vulnerability Scanning Project

This folder contains scans and notes related to vulnerability assessment of the Metasploitable 2 vulnerable virtual machine.

## Project Overview

Metasploitable 2 is an intentionally vulnerable Linux VM designed for practicing penetration testing and vulnerability scanning.

## Contents

- `output_files/`: Scan results from Nessus and other tools.
- `screenshots/`: Images of setup and scan outputs.
- `notes.md`: Additional observations and troubleshooting notes.

## How to Use

1. Set up Metasploitable 2 VM in your virtualization environment.
2. Run vulnerability scans against the VM’s IP.
3. Save scan output files in the `output_files/` directory.
4. Document your findings and observations in `notes.md`.

---

This project is part of hands-on learning for cybersecurity vulnerability assessment.

## Nessus Vulnerability Scan Results on Metasploitable2

After setting up Metasploitable2 and configuring Nessus, I ran a vulnerability scan targeting the VM’s IP address.

### Key Finding:

- **High Severity:** Samba Badlock vulnerability (CVE-2016-2118)  
  This critical vulnerability allows attackers to intercept and manipulate Samba traffic, potentially leading to privilege escalation.

### Other Observations:
- Open ports include SSH (22), HTTP (80), SMB (139/445), among others.
- Multiple medium and low severity vulnerabilities were also identified.

---

These results validate that Metasploitable2 is an effective test target for vulnerability scanning practice.
