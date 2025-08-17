from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

#sniffing

sniff(prn = packet_callback,store=False)