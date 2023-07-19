import nmap
import socket
class HostName:
    network = ""
    def set_value(self,n):
        self.network = n
    def get_hostname(self):
        nm = nmap.PortScanner()
        a = nm.scan(self.network,arguments="-O")
        ips = []
        for key,value in a['scan'].items():
            ips.append(value['addresses']['ipv4'])
        for ip in ips:
            try:
                print(f"{ip} -> {socket.gethostbyaddr(ip)[0]}")
            except:
                print(f"{ip} Hostname not found!")

