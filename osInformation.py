import nmap
class OsScan:
    network = ""
    def set_value(self,n):
        self.network = n
    def get_os(self):
        nm = nmap.PortScanner()
        a = nm.scan(self.network,arguments="-O")
        for key,value in a['scan'].items():
            print(f"[+] Ip: {value['addresses']['ipv4']}")
            os_= value['osmatch']
            print("[+] OS:")
            for i in os_:
                print(i['name'])

