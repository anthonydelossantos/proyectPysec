from getmac import get_mac_address as gmac

class GMac:
    ip_addr = ""
    def set_value(self,ip):
        self.ip_addr = ip
    def get_ipMac(self):
        ip_tmp= gmac(ip=self.ip_addr)
        return ip_tmp
    def get_ownMac(self):
        return gmac()

