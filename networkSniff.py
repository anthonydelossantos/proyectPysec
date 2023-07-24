from scapy.all import sniff, ICMP,TCP,IP,DNS,ARP
import keyboard


'''
Category Events:
0 -> Informative
1 -> Warning
2 -> Critical

Malicious Events: 5
Critical: 4
Warning: 1

Critical Events.
-----------------------------------------------------------------------------------------------------
event 0: Malicious Connection to 0.0.0.0 C2 - Critical
event 1: Malicious Connection to 0.0.0.0 C2 - Critical
event 2: Malicious Connection to 0.0.0.0 C2 - Critical
event 3: Port Scanning - Critical

----------------------------------------------------------------------------------------------------
Warning Events.
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Informative Events.
----------------------------------------------------------------------------------------------------
event 0: Scanning the Network - informative

-----------------------------------------------------------------------------------------------------


'''




class MalSniffer:
    packetsLimit = 100
    packetCount = 0
    informative = []
    Warning_log = []
    critical = []
    malMAC = ""
    stop_sniff = False

    def detect_syn_scan(self,packet):
        category_event = 1
        if TCP in packet and packet[TCP].flags == 2:  # Verificamos si el paquete es TCP y tiene el flag SYN (2)
            msg="SYN port Scan from {} to the port {}. Warning".format(packet["IP"].src, packet['TCP' ].dport)
            self.Warning_log.append(msg)


    def detect_requests(self,packet):
        c2list = []
        count = 0
        with open('c2_serversIP.txt','r') as c2f:
                category_event = 2
                l = c2f.readlines()
                for line in l:
                    if  not line.isspace():
                        line = line.replace('\n','')
                        c2list.append(line)
        print(packet.summary())
        for i in c2list:
            ip = i.split(":")[0]
            port = i.split(":")[1]
            if TCP in packet and packet[IP].dst ==  ip :
                msg = f"Malicious Connection to {ip} C2 - Critical"
                self.critical.append(msg)

    def detect_arp_packets(self,packet):
        
        if ARP in packet :
            self.packetCount +=1
            if self.packetCount > self.packetsLimit:
                if self.packetCount > 95:
                    msg =f"Malicious activity from {packet[ARP].hwsrc}. More than {self.packetCount} ARP packets detected from this host - Informative"
                    self.informative.append(msg)
            



    def allDectection(self,packett):
        self.detect_arp_packets(packett)
        self.detect_syn_scan(packett)
        self.detect_requests(packett)
    def stop_sniffing():
        global stop_sniff
        stop_sniff = True
            