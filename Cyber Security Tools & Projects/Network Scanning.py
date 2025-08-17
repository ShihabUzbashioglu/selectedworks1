from scapy.all import ARP,Ether ,srp

# 192.168.1.1/24

def arp_scan(ip):
    arp_pack = ARP(pdst=ip)
    ether_frame = Ether (data="FF-FF-FF-FF-FF-FF")

    arp_req = ether_frame / arp_pack

    result = srp(arp_req,timeout=2,verdose=False)[0]
    devices = []

    for sent,recieved in result :
        devices.append('ip : ' recieved.psrc, 'mac :' recieved.hwsrc)
    return devices


ip_range = "192.168.1.1/24"
devices = arp_scan(ip_range)

for device in devices:
    print(f'IP :{devices['ip']}, MAC :{devices['mac']}')