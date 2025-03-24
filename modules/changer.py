import subprocess

def mac_changer(new_mac, interface):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")
    try:
        subprocess.check_call(["ifconfig", interface, "down"])
        subprocess.check_call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.check_call(["ifconfig", interface, "up"])
    except subprocess.CalledProcessError as e:
        print(f"[+] Failed to change MAC Address. {e}")