from scapy.all import sr1, IP, TCP
import socket 

class Scanner:
    target_ip = ""
    port = 0

    def set_value(self,port1,ip):
        self.target_ip = ip
        self.port = port1

    def scan_port(self):
        packet = IP(dst=self.target_ip) / TCP(dport=self.port, flags="S")
        response = sr1(packet, timeout=1, verbose=False)
        try:
            service = socket.getservbyport(self.port)
        except: 
            service = "Unknown"
        print("[+] Port\tStatus\tService")
        if response and response[TCP].flags == "SA":
            print(f"[+] {self.port}\t\tOPEN\t{service}")
        else:
            print(f"[+] {self.port}\tCLOSED\t{service}")

