#import networkSniff
import websiteInfo
import geolocator
import Macaddres
import hostnameInformation, osInformation,interfaces,scanPorts
import smtMail
import config
import time
#TODO cambiar inputs fuera de los metodos
class Main:
    def set_value(self,opc):
        self.option = opc
    def printstr(self,msg):
        print(msg)
    def menu(self):
        banner = '''
   _______    _______     ______  ___  ___  _______   ______  ___________  ______    _______  
  |   __ "\  /"      \   /    " \|"  \/"  |/"     "| /" _  "\("     _   ")/    " \  /"     "| 
  (. |__) :)|:        | // ____  \\   \  /(: ______)(: ( \___))__/  \\__/// ____  \(: ______) 
  |:  ____/ |_____/   )/  /    ) :)\\  \/  \/    |   \/ \        \\_ /  /  /    ) :)\/    |   
  (|  /      //      /(: (____/ // /   /   // ___)_  //  \ _     |.  | (: (____/ // // ___)   
 /|__/ \    |:  __   \ \        / /   /   (:      "|(:   _) \    \:  |  \        / (:  (      
(_______)   |__|  \___) \"_____/ |___/     \_______) \_______)    \__|   \"_____/   \__/      
                                                                                              '''
        options = '''\n
1) Analize Network Traffic 
2) Gather Website information (IP,NameServer,etc)
3) Geolocation (IP)
4) Scan multiple ports
5) Scan a single port
6) Get the MAC address 
7) Get all devices OS in a network
8) Get all devices hostname in a network
9) Get all interfaces 
10) Send secret mail
11) Exit
'''
        self.printstr(banner)
        self.printstr(options)
    def quit(self):
        if self.option == 11:
            return True
        else:
            return False
    def analizeTraffic(self):
        self.printstr("Analizing the traffic...")
    def getWebInfo(self):
        webinfo = websiteInfo.Webinfo()
        n = input("Introduce the URL here -> ")
        webinfo.set_value(n)
        res = webinfo.ns_lookup()
        host = webinfo.get_hostname()
        ipvv6 = webinfo.get_ipv6()
        zone = webinfo.get_zone()
        if res :
            self.printstr(f"IPv4 of {n} is {res}")
        if host:
            self.printstr(f"Domain Name Server of {n} is {host}")
        if ipvv6:
            self.printstr(f"IPv6 from {n} is {ipvv6}")
        elif ipvv6 ==False:
            self.printstr(f"We can not obtain IPv6 from {n}")
        if zone :
            print("Zone information: ")
            for z in zone:
                print(z)
    def geolocation(self,option):
        geo = geolocator.Geolocator()
        if option == 1:
            geo.get_ownLocation()
        elif option == 2:
            ip_victim = input("Introduce the victim ip -> ")
            geo.set_value(ip_victim)
            geo.get_geoLocation(ip_victim)
 
    def scMPorts(self,port,ip):
        scanner = scanPorts.Scanner()
        scanner.set_value(port,ip)
        scanner.scan_port()
    def scSPort(self):
        self.printstr("Scanning a Single Port...")
    def get_MAC(self,ip):
        #TODO verificar que una ip introducida sea valida
        objM = Macaddres.GMac()
        objM.set_value(ip)
        if ip == "127.0.0.1":
            print(f"[+] My own MAC address if {objM.get_ownMac()}")
        else:
            print(f"[+] The MAC address of {ip} is {objM.get_ipMac()}")
        
    def getOSInfo(self,net):
        oI = osInformation.OsScan()
        oI.set_value(net)
        oI.get_os()
    def getHostnameInfo(self,net):
        HMain = hostnameInformation.HostName()
        HMain.set_value(net)
        HMain.get_hostname()
    def getInterfaces(self):
        intr = interfaces.Interface()
        intr.get_status()
        
    def sendSecretM(self):
        self.printstr("Hi. Welcome to email sender...")
        sender_email = config.email
        self.printstr("[From] -> proyectoprogram007@outlook.com ")
        receiver_email = input("[to] -> ")
        message = input("[Body] -> ")
        sender_password = config.password
        subject = input("[Subject] -> ")
        m = smtMail.Mail()
        m.set_values(sender_email, sender_password, receiver_email, subject, message)
        m.set_connection()
        try:
            m.send_email()
            m.send_encryptMail()
        except:
            print("Oops Something goes wrong")


if __name__ == '__main__':
    try:
        objMain = Main()
        
        while True:
            objMain.menu()
            opc = int(input("Choose a number [1-10] -> "))
            objMain.set_value(opc)
            if opc == 1:
                print("pronto")
            elif opc == 2:
                objMain.getWebInfo()
            elif opc == 3:
                option = int(input("Choose what you gonna do? 1) Get my own Geolocation 2) Get a victim Geolocation.\n-> "))
                objMain.geolocation(option)
            elif opc == 4:
                print("Introduce range of ports: ")
                first_port = int(input("Initial port-> "))
                last_port = int(input("Last port -> "))
                ipaddr = input("Victim IP -> ")
                for i in range(first_port,last_port):
                    objMain.scMPorts(i,ipaddr)
                

            elif opc == 5:
                one_port = int(input("port-> "))
                ipaddr = input("Victim IP -> ")
                objMain.scMPorts(one_port,ipaddr)

            elif opc == 6:
                ip_opc = input("Introduce a IP address or just introduce 127.0.0.1 if you want to know what is your own MAC address -> ")
                objMain.get_MAC(ip=ip_opc)

            elif opc == 7:
                net = input("Introduce the network with the CDIR (192.168.3.0/24) -> ")
                objMain.getOSInfo(net)
                
            elif opc == 8:
                 net = input("Introduce the network with the CDIR (192.168.3.0/24) -> ")
                 objMain.getHostnameInfo(net)

            elif opc == 9:
                objMain.getInterfaces()

            elif opc == 10:
                objMain.sendSecretM()

            if objMain.quit():
                print("bye.")
                break
            time.sleep(3)


        
    except:
        print("")