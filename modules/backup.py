import json
import os

BACKUP_FILE = "mac_backup.json"

def backup_mac(interface, mac):
    data = {interface: mac}
    try:
        with open(BACKUP_FILE, 'w') as f:
            json.dump(data, f)
        print(f"[+] Original MAC address backed up: {mac}")
    except Exception as e:
        print(f"[-] ERROR: Failed to backup MAC. {e}")

def load_backup(interface):
    if not os.path.exists(BACKUP_FILE):
        print("[-] No backup file found.")
        return None
    try:
        with open(BACKUP_FILE, 'r') as f:
            data = json.load(f)
        return data.get(interface, None)
    except Exception as e:
        print(f"[-] ERROR: Failed to load backup. {e}")
        return None
