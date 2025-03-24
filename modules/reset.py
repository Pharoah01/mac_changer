import re
import subprocess

def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface]).decode()
        mac_search = re.search(r"([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})", output)
        if mac_search:
            return mac_search.group()
    except Exception as e:
        print(f"[-] ERROR: Failed to retrieve MAC. {e}")
    return None


def reset_mac(interface, original_mac):
    print(f"[+] Resetting MAC address for {interface} to original: {original_mac}")
    try:
        subprocess.check_call(["ifconfig", interface, "down"])
        subprocess.check_call(["ifconfig", interface, "hw", "ether", original_mac])
        subprocess.check_call(["ifconfig", interface, "up"])
        print("[+] MAC address reset successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[-] ERROR: Failed to reset MAC address. {e}")