import re

def is_valid_mac(mac):
    if re.match(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$", mac):
        return True
    return False