import random

def random_mac():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    mac[0] = (mac[0] | 0x02) & 0xfe  # Set locally administered & unicast
    return ":".join(f"{byte:02x}" for byte in mac)
