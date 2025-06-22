# 🔎 Nmap Scan Examples

This folder contains saved Nmap scan results and the commands used to generate them. These examples are useful for reference, analysis, and learning how different scan types work.

---

## 📄 Files & Descriptions

### `basic_scan.txt`
- **Description**: Service version detection scan of `scanme.nmap.org`
- **Command Used**:

```bash
nmap -sV scanme.nmap.org -oN basic_scan.txt
