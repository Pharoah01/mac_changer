import argparse

def get_args():
    parser = argparse.ArgumentParser(description="[+] Simple MAC Changer Tool!!")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g: eth0, wlan0 etc..)")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-m", "--mac", help="New MAC Address to be changed to ....")
    group.add_argument("-r", "--random", help="Generate a random MAC Address", action="store_true")
    group.add_argument("--reset", help="Reset back to original MAC Address", action="store_true")

    return parser.parse_args()
