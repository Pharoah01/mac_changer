# Mac_Changer

# MAC Changer Tool 🛠️

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple Python-based MAC (Media Access Control) address changer tool. This tool allows you to change your MAC address to a custom value, generate a random MAC, or reset it to the original value.

---

## 🚀 Features
✅ Change MAC address to a user-specified address  
✅ Generate and assign a random MAC address  
✅ Reset MAC to its original hardware address  
✅ Validate MAC address format  
✅ Check for valid network interfaces  
✅ Modular structure for easier maintenance

---

## 🐍 Requirements

- Python 3.x
- Linux system (for `ifconfig` and `ip` command usage)
- `net-tools` package (`ifconfig`)
- `sudo` privileges to run commands

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/mac-changer-tool.git
cd mac-changer-tool

sudo apt update
sudo apt install net-tools -y

🧩 Project Structure

mac-changer-tool/
│
├── modules/
│   ├── changer.py
│   ├── interface_checker.py
│   ├── parser.py
│   ├── random_mac.py
│   ├── reset.py
│   └── validator.py
│
├── main.py
├── README.md
└── requirements.txt (optional)


⚙️ Usage

🔵 Change MAC address manually
```bash
sudo python3 main.py -i eth0 -m 00:11:22:33:44:55

🟣 Generate and apply a random MAC address
```bash
sudo python3 main.py -i eth0 --random

🟢 Reset to the original MAC address
```bash
sudo python3 main.py -i eth0 --reset
⚠️ Replace eth0 with your actual network interface (e.g., wlan0, ens33).

🎯 Python Argument Parser Help
```bash
sudo python3 main.py -h

[+] Simple MAC Changer Tool!!

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Network interface (e.g: eth0, wlan0 etc..)
  -m MAC, --mac MAC     New MAC Address to be changed to ....
  -r, --random          Generate a random MAC Address
  --reset               Reset back to original MAC Address

⚠️ Notes

    Designed for Linux systems only.

    Requires root privileges (sudo).

    Ensure correct network interface with ip link or ifconfig.

👨‍💻 Author:

[Pharoah01] | [pharoah.in.net] | [www.linkedin.com/in/elavarasan-t-a5971b2a5]