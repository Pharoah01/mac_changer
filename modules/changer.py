import subprocess
import sys

def mac_changer(new_mac, interface):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")
    try:
        subprocess.check_call(["ip", "link", "set", "dev", interface, "down"])
        subprocess.check_call(["ip", "link", "set", "dev", interface, "address", new_mac])
        subprocess.check_call(["ip", "link", "set", "dev", interface, "up"])
        print("[+] MAC address successfully changed!")
    except subprocess.CalledProcessError as e:
        print(f"[-] ERROR: Failed to change MAC Address. {e}")
        sys.exit(1)