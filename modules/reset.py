import re
import subprocess
import json
import os


BACKUP_FILE = "mac_backup.json"


def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface]).decode()
        mac_search = re.search(r"([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})", output)
        if mac_search:
            return mac_search.group()
    except Exception as e:
        print(f"[-] ERROR: Failed to retrieve MAC. {e}")
    return None


def backup_original_mac(interface):
    original_mac = get_current_mac(interface)
    if original_mac:
        data = {interface: original_mac}
        with open(BACKUP_FILE, "w") as f:
            json.dump(data, f)
        print(f"[+] Original MAC address backed up: {original_mac}")
    else:
        print("[-] Could not backup original MAC.")


def load_original_mac(interface):
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "r") as f:
            data = json.load(f)
        return data.get(interface)
    else:
        print("[-] Backup file not found.")
    return None


def reset_mac(interface):
    original_mac = load_original_mac(interface)
    if not original_mac:
        print("[-] No backup found for this interface.")
        return

    print(f"[+] Resetting MAC address for {interface} to original: {original_mac}")
    try:
        subprocess.check_call(["ifconfig", interface, "down"])
        subprocess.check_call(["ifconfig", interface, "hw", "ether", original_mac])
        subprocess.check_call(["ifconfig", interface, "up"])
        print("[+] MAC address reset successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[-] ERROR: Failed to reset MAC address. {e}")
