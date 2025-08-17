from scapy.all import sniff,ip,udp,tcp


def packet_callback(packet):
    if ip in packet:
        ip_src = packet[ip].src
        ip_dst = packet[ip].dst
        proto = packet[ip].proto

        print(f'\n[+] New Packet : {ip_src} -> {ip_dst} | Protocol : {proto}')

        if TCP In packet :
            sport = packet[TCP].sport
            dport = packet[tcp].dport
            print(f' TCP | Src Port : {sport} -> Dst Port : {dport}')

        elif UDP In packet :
            sport = packet[UDP].sport
            dport = packet[UDP].dport

            print(f'       UDP  | SRC PORT : {sport}      ->    Dst Port : {dport}')


sniff(prn=packet_callback,store=False)