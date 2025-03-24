#!/usr/bin/env python3

import re
from modules import parser, validator, interface_checker, changer, random_mac, reset

def is_valid_interface_name(name):
    return re.match(r"^[a-zA-Z0-9_.-]+$", name) is not None

def main():
    args = parser.get_args()

    if not is_valid_interface_name(args.interface):
        print(f"[-] ERROR: Invalid interface name '{args.interface}'.")
        return

    if not interface_checker.interface_check(args.interface):
        print(f"[-] ERROR: Network Interface '{args.interface}' not found.")
        return

    if args.random and args.mac:
        print("[-] ERROR: Cannot use both --random and --mac options together.")
        return

    original_mac = reset.get_current_mac(args.interface)

    if args.reset:
        if original_mac:
            reset.reset_mac(args.interface, original_mac)
        else:
            print(f"[-] Could not find original MAC to reset to.")
        return

    if args.random:
        mac = random_mac.random_mac()
        print(f"[+] Generated random MAC Address: {mac}")
    else:
        mac = args.mac

    if not validator.is_valid_mac(mac):
        print("[-] ERROR: Invalid MAC address format. Use format like 00:11:22:33:44:55")
        return

    changer.mac_changer(mac, args.interface)

    print("[+] MAC address successfully changed!")

if __name__ == "__main__":
    main()