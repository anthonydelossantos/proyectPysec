from scapy.all import sniff, ICMP,TCP,IP

def detect_ping(packet):
    if ICMP in packet and packet[ICMP].type == 8:  # 8 corresponde a los paquetes ICMP de tipo 'Echo Request' (ping)
        print("Se detectó un ping en la red desde {} hacia {}.".format(packet['IP'].src, packet['IP'].dst))
def detect_syn_scan(packet):
    if TCP in packet and packet[TCP].flags == 2:  # Verificamos si el paquete es TCP y tiene el flag SYN (2)
        print("Se detectó un escaneo de puertos SYN desde {} hacia el puerto {}.".format(packet["IP"].src, packet['TCP' ].dport))

try:
    sniff(filter="tcp", prn=detect_syn_scan,timeout=60)
   
except KeyboardInterrupt :
    print("chao")