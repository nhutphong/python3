#!/usr/bin/env python3

import subprocess as sp

default_mac_eth0 = "18:03:73:83:9b:c2"
default_mac_wlan0 = "94:39:e5:d2:40:2b"

interface = input("interface > ")
new_mac = input("new MAC > ")

print("[+] Changing Mac address for " + interface + " to " + new_mac)

sp.call(["ifconfig ", interface, "down"])
sp.call(["ifconfig", interface, "hw ether", new_mac])
sp.call(["ifconfig", interface. "up"])

