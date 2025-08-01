# Nessus Scan Configuration for Metasploitable2

This document summarizes the settings used for the Nessus vulnerability scan against the Metasploitable2 VM.

## Scan Details

- **Scan Template:** Advanced Scan  
- **Target IP:** `192.168.0.45`  
- **Discovery Settings:**  
  - *Ping the remote host*: **Disabled**  
  - *ARP ping*: **Disabled**   
- **Port Scanning:**  
  - Ports scanned: `22, 80, 139, 445`  
  - Treat unscanned ports as closed: **Enabled**  
- **Assessment:**  
  - Service detection: **Enabled**  
  - OS detection: **Enabled**  
  - Vulnerability scanning: **Enabled**

---

## Output

The full scan report is saved in the subfolder:  
`nessus/metasploitable2/scan_reports/`

Files include:  
- `nessus_scan_report.html` (detailed HTML report)  

---

This setup allows reproducible scans and easy reference for future assessments.
