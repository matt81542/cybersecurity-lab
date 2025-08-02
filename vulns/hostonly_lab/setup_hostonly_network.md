# Setting Up a Host-Only Virtual Network in VirtualBox

To isolate virtual machines for scanning and testing (e.g. with Nessus or Metasploit), a **Host-Only** VirtualBox network is recommended. This keeps lab traffic off your main network and avoids IP conflicts.

---

## Why Use Host-Only?

- Isolates VM traffic from the internet and home network.
- Allows scanning tools like Nessus to target VMs without exposing your main devices.
- Ensures consistent IP ranges for internal lab testing.

---

## Step-by-Step: Create Host-Only Network

1. **Open VirtualBox**  
   Go to **File → Tools → Network Manager**.

2. **Add a New Host-Only Network**
   - Click **Create**.
   - You'll see something like: `vboxnet0`.

3. **Configure the Network**
   - Click the **gear icon** next to the new adapter.
   - Suggested settings:
     - **IPv4 Address**: `192.168.56.1`
     - **IPv4 Network Mask**: `255.255.255.0`
     - **DHCP Server**: **Disable**
   - Save and close.

4. **Assign to VM**
   - Select your VM → **Settings → Network**.
   - Enable **Adapter 2**.
   - Attach to: `Host-Only Adapter`.
   - Name: Select the one you just created (e.g. `vboxnet0`).

---

## Notes

- Ensure the IP range does **not** overlap with your real network (e.g. if your LAN is `192.168.170.x`, use something like `192.168.56.x` for host-only).
- Assign static IPs within the VM (e.g. `192.168.56.10` for Kali, `192.168.56.20` for Metasploitable).

---

## Example

| Device          | IP Address       | Notes                  |
|-----------------|------------------|-------------------------|
| Host machine    | `192.168.170.x`  | On your real LAN        |
| VBox Host-only  | `192.168.56.1`   | VirtualBox interface    |

---

## Troubleshooting

- If VMs can't ping each other:
  - Check VM firewall settings.
  - Ensure correct adapter is selected in VirtualBox.
  - Check that static IPs are on the same subnet.

