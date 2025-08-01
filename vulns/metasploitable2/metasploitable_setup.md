# Setting Up Metasploitable2 in VirtualBox

To test vulnerability scans in a controlled environment, I set up **Metasploitable2** using **VirtualBox**. Here's how:

## Prerequisites
- [VirtualBox](https://www.virtualbox.org/) installed
- [Metasploitable2 VM](https://sourceforge.net/projects/metasploitable/) downloaded (as a `.zip` archive)

## Setup Steps

1. **Extract the Metasploitable2 archive**  
   After downloading, unzip the folder to your desired location.

2. **Import the VM into VirtualBox**  
   Open VirtualBox → *Machine* → *Add* → Select `Metasploitable.vmx` or create a new VM and attach the `.vmdk` file as the hard disk.

3. **Network Configuration**  
   Go to **Settings > Network**  
   Set **Adapter 1** to:  
   - **Attached to:** *Bridged Adapter* (recommended for host visibility)  
   - OR **Host-only Adapter** if isolating the VM from the wider network  
   Ensure the host and VM are on the **same subnet** (e.g., `192.168.0.X`).

4. **Start the VM**  
   Login with default credentials:  
   - **Username:** `msfadmin`  
   - **Password:** `msfadmin`

5. **Confirm Network Connectivity**  
   Ping the host from the VM and vice versa:  
   ```bash
   ping <host_ip>
   ping <vm_ip>
