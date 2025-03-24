import subprocess

def interface_check(interface):
    try:
        subprocess.check_output(["ip", "link", "show", interface])
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] ERROR: Interface check failed with: {e}")
        return False
