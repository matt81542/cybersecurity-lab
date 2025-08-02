# OWASP BWA Nessus Vulnerability Scan

This project documents the setup and vulnerability scanning of the OWASP Broken Web Applications (BWA) virtual machine using Nessus.


## 🖥️ Virtual Machine Setup

1. **Downloaded VM:**  
   OWASP Broken Web Applications Project (BWA)  
   [https://sourceforge.net/projects/owaspbwa/](https://sourceforge.net/projects/owaspbwa/)

2. **Imported into VirtualBox:**
   - Created a new VM and attached `.vmdk` as virtual hard disk

3. **Networking Configuration (Host-Only):**
   - VirtualBox → File → Host Network Manager
     - Created a new Host-Only network (`VirtualBox Host-Only Ethernet Adapter`)
     - DHCP: Disabled
     - IPv4 Address: `192.168.56.101`
     - IPv4 Network Mask: `255.255.255.0`
   - VM → Settings → Network
     - Adapter 1: Attached to Host-Only Adapter

4. **Booted VM and confirmed IP:**
   ```bash
   ip a
   ```
## 🔍 Nessus Scan Instructions

1. **Start Nessus on the host machine:**

   Open a web browser and go to:

2. **Log in to Nessus.**

3. **Create a new scan:**
- Click **"New Scan"**
- Choose **"Advanced Network Scan"**

4. **Configure the scan:**
- **Name:** OWASP BWA Scan (or any name you prefer)
- **Targets:** 
  ```
  192.168.56.101
  ```
  (This is the IP address of the OWASP BWA VM)

5. **Save the scan.**

6. **Launch the scan:**
- Click the scan name
- Click **"Launch"**

7. **After the scan completes:**
- Click the completed scan
- Click **"Export"** > **"As HTML"**
- Save the file in:
  ```
  scan_reports/owasp_bwa_report.html
  ```

> Make sure the OWASP BWA VM is running and reachable before launching the scan.

8. **Upload the scan report to GitHub:**
   - Go to your repository folder
   - Place the exported HTML report in:
     ```
     vulns/owasp_bwa/scan_reports/
     ```

## ✅ Notes
- The IP `192.168.56.101` is based on the Host-Only Adapter range. If you use a different host-only network, your IP may vary.
- If Nessus can't reach the target, verify that both the host and VM are on the same virtual network and that the target VM has networking enabled (and firewalls aren't blocking it).


