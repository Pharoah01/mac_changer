#!/bin/bash

function usage() {
    echo "Usage: $0 -i <interface> [-m <mac> | -r | --reset]"
    echo "  -i  Network interface (e.g., eth0, wlan0)"
    echo "  -m  Specific MAC address (e.g., 00:11:22:33:44:55)"
    echo "  -r  Generate random MAC address"
    echo "  --reset  Reset to original MAC address"
    exit 1
}

function is_valid_mac() {
    if [[ "$1" =~ ^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$ ]]; then
        return 0
    else
        return 1
    fi
}

function random_mac() {
    printf '%.2x:%.2x:%.2x:%.2x:%.2x:%.2x\n' $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256))
}

function backup_mac() {
    ifconfig "$1" | grep ether | awk '{print $2}' > "/tmp/${1}_mac_backup"
    echo "[+] Backed up original MAC to /tmp/${1}_mac_backup"
}

function load_backup_mac() {
    if [ -f "/tmp/${1}_mac_backup" ]; then
        cat "/tmp/${1}_mac_backup"
    else
        echo ""
    fi
}

function change_mac() {
    local iface="$1"
    local new_mac="$2"
    echo "[+] Changing MAC Address for $iface to $new_mac"
    sudo ifconfig "$iface" down
    sudo ifconfig "$iface" hw ether "$new_mac"
    sudo ifconfig "$iface" up
}


INTERFACE=""
MAC=""
RANDOM_FLAG=0
RESET_FLAG=0

while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -i)
            INTERFACE="$2"
            shift; shift ;;
        -m)
            MAC="$2"
            shift; shift ;;
        -r)
            RANDOM_FLAG=1
            shift ;;
        --reset)
            RESET_FLAG=1
            shift ;;
        *)
            usage ;;
    esac
done

if [ -z "$INTERFACE" ]; then
    usage
fi


if [ "$RANDOM_FLAG" -eq 1 ] && [ -n "$MAC" ]; then
    echo "[-] ERROR: Cannot use --random and --mac together."
    exit 1
fi

if [ "$RESET_FLAG" -eq 1 ]; then
    OLD_MAC=$(load_backup_mac "$INTERFACE")
    if [ -n "$OLD_MAC" ]; then
        change_mac "$INTERFACE" "$OLD_MAC"
        echo "[+] MAC reset to original: $OLD_MAC"
    else
        echo "[-] No backup found to reset for $INTERFACE."
    fi
    exit 0
fi

if [ "$RANDOM_FLAG" -eq 1 ]; then
    MAC=$(random_mac)
    echo "[+] Generated random MAC: $MAC"
fi

if ! is_valid_mac "$MAC"; then
    echo "[-] ERROR: Invalid MAC format. Use format like 00:11:22:33:44:55"
    exit 1
fi

backup_mac "$INTERFACE"
change_mac "$INTERFACE" "$MAC"
echo "[+] MAC address successfully changed!"

