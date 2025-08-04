# Setting Up Greenbone Vulnerability Management (GVM) on Kali Linux

This guide walks through the process of installing and setting up GVM (Greenbone Vulnerability Management) on Kali Linux — a powerful open-source vulnerability scanning and management tool.

## 🖥️ System Requirements

- Kali Linux VM or bare-metal install
- Internet connection
- Sudo/root access

---

## 🔧 Step 1: Update Your System

Keep the package list and system up to date:

```bash
sudo apt update && sudo apt full-upgrade -y
```
📦 Step 2: Install GVM
Install Greenbone Vulnerability Management from Kali’s repository:

bash
Copy
Edit
sudo apt install -y gvm
🔄 Step 3: Run the Setup Script
Once installed, run the GVM setup script:

sudo gvm-setup

This step:
Creates a GVM admin user
Generates certificates and config files
Downloads vulnerability feed data

⚠️ At the end of the setup, note the password that is displayed for the admin user — it looks like a UUID and is required to log in to the web interface.

🔐 Example Password Output

[*] Please note the password for the admin user
[*] User created with password '5d4e2b62-3412-4b01-ba98-e63dd2912172'
✅ Step 4: Verify Setup
Run the check script to ensure everything is configured correctly:

bash
Copy
Edit
sudo gvm-check-setup
Look for all [OK] messages. If anything is marked [ERROR] or [WARNING], follow the guidance provided in the output to fix the issue.
