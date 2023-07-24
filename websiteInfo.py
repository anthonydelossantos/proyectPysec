import socket 
import dns.resolver
from urllib.parse import urlparse

class Webinfo:
    domain=""

    def set_value(self,domain):
        if bool(urlparse(domain).scheme):
            parsed_url = urlparse(domain)
            hostname = parsed_url.hostname
            if hostname.startswith("www."):
                hostname = hostname[4:] 
            self.domain = hostname
        else:
            self.domain = domain
        
    def ns_lookup(self):
        try:
            ip = socket.gethostbyname(self.domain)
            return ip 
        except :
            return False
        
    def get_hostname(self):
        try:
            hostname = socket.getfqdn(self.domain)
            return hostname
        except:
            return False
        
    def get_ipv6(self):
        try:
            ipv6 = socket.getaddrinfo(self.domain, port=80)
            return ipv6[3][4][0]
        except:
            return False
    def get_zone(self):
        try:
            answers = dns.resolver.resolve(self.domain, 'SOA')
            return answers
        except:
            return False




