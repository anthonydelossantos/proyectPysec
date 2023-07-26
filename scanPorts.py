from scapy.all import sr1, IP, TCP
import socket 

class Scanner:
    target_ip = ""
    port = 0

    def set_value(self,port1,ip):
        self.target_ip = ip
        self.port = port1

    def scan_port(self):
        msg = ""
        packet = IP(dst=self.target_ip) / TCP(dport=self.port, flags="S")
        response = sr1(packet, timeout=1, verbose=False)
        try:
            service = socket.getservbyport(self.port)
        except: 
            service = "Unknown"
        msg = ""
        if response and response[TCP].flags == "SA":
            msg += f"\n[+] {self.port}\t\tOPEN\t{service}"
            return msg
        else:
            msg+= f"\n[+] {self.port}\tCLOSED\t{service}"
            return msg

