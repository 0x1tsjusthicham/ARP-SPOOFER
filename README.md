# ARP Spoofer

This Python script performs an ARP spoofing attack to intercept traffic between a target device and a router. It continuously sends spoofed ARP replies, tricking the target and router into thinking the attacker's machine is the other device.

## Prerequisites

You will need:
- **Python 3.x**
- **Scapy** library installed

You can install Scapy with:
pip install scapy

## Usage

Run the script by specifying the target (victim) IP address and the router (gateway) IP address like so:
sudo python3 arp_spoofer.py -t [target_ip] -r [router_ip]

Replace [target_ip] with the victim’s IP and [router_ip] with the router's IP.

### Example:
sudo python3 arp_spoofer.py -t 192.168.1.5 -r 192.168.1.1

### Output:
The script will send packets continuously, outputting:
[+] 2 Packet Sent
[+] 2 Packet Sent

## Code Overview
1. get_arguments(): Parses command-line arguments for the victim and router IPs.
2. get_mac(): Sends ARP requests to get the MAC address of the target or router.
3. spoof(): Sends a spoofed ARP response to impersonate the target and router.
4. restore(): Restores the correct ARP mapping when the script is stopped.

## Important Notes

- The script requires root privileges to run. Use sudo before the command.
- ARP spoofing can disrupt network communication. Be cautious when running this script.

## License
@itsjusthicham