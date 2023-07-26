from scapy.all import sniff
import websiteInfo
import geolocator
import Macaddres
import hostnameInformation, osInformation,interfaces,scanPorts,networkSniff
import smtMail
import config
import time




class Main:
    option = ""
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
        ns = networkSniff.MalSniffer()
        try:
            sniff(filter="tcp and arp", prn=ns.allDectection, stop_filter=ns.stop_sniff)
            with open('report.txt','w') as report:
                report.write('''
        _______    _______    _______    ______     _______  ___________  
        /"      \  /"     "|  |   __ "\  /    " \   /"      \("     _   ") 
        |:        |(: ______)  (. |__) :)// ____  \ |:        |)__/  \\__/  
        |_____/   ) \/    |    |:  ____//  /    ) :)|_____/   )   \\_ /     
        //      /  // ___)_   (|  /   (: (____/ //  //      /    |.  |     
        |:  __   \ (:      "| /|__/ \   \        /  |:  __   \    \:  |     
        |__|  \___) \_______)(_______)   \"_____/   |__|  \___)    \__|     
                                                                        
        ''')
                report.write("\n\n")
                if len(ns.Warning_log) > 0:
                    report.write("\nWarning Events.\n----------------------------------------------------------------------------------------------------\n")
                    for warn in ns.Warning_log:
                        report.write(f"\n{warn}\n")
                    report.write("\n----------------------------------------------------------------------------------------------------\n")
                elif  len(ns.Warning_log) == 0:
                    report.write("\nWarning Events.\n----------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------\n")  
                if len(ns.critical) >0 :
                    report.write("\nCritical Events.\n----------------------------------------------------------------------------------------------------\n")
                    for crit in ns.critical:
                        report.write(f"\n{crit}\n")
                    report.write("\n----------------------------------------------------------------------------------------------------\n")
                elif len(ns.critical)  == 0:
                    report.write("\nCritical Events.\n----------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------\n")

                    
                if len(ns.informative) > 0:
                    report.write("\nInformative Events.\n----------------------------------------------------------------------------------------------------\n")
                    for inf in ns.informative:
                        report.write(f"\n{inf}\n")
                    report.write("\n----------------------------------------------------------------------------------------------------\n")
                elif len(ns.informative) == 0:
                    report.write("\nInformative Events.\n----------------------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------------------\n")
            print("Logs Wrote.") 
            print("Sending the Report.")
            sender_email = config.email
            print(f"[From] -> {sender_email} ")
            receiver_email = input("[to] -> [defaul: testh892@gmail.com] ")
            if receiver_email == "":
                receiver_email = "testh892@gmail.com"
            sender_password = config.password
            subject = input("[Subject] -> ")
            message = ""
            attach = "report.txt"
            m = smtMail.Mail()
            m.set_values(sender_email, sender_password, receiver_email, subject, message,attach)
            m.set_connection()  
            m.send_mailAttach()

           
        
        except KeyboardInterrupt:
            pass
            
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
 
    def scPorts(self,port,ip):
        scanner = scanPorts.Scanner()
        scanner.set_value(port,ip)
        scanner.scan_port()
    def get_MAC(self,ip):
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
        self.printstr(f"[From] -> {sender_email} ")
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
        logs = []
        while True:
            objMain.menu()
            opc = int(input("Choose a number [1-10] -> "))
            while opc not in range(1,12):
                opc = int(input("Choose a number [1-10] -> "))

            objMain.set_value(opc)
            if opc == 1:
                objMain.analizeTraffic()
                if "Traffic Sniffing" not in logs:
                    logs.append("Traffic Sniffing")
            elif opc == 2:
                objMain.getWebInfo()
                if "Gather Web Info" not in logs:
                    logs.append("Gather Web Info")
            elif opc == 3:
                option = int(input("Choose what you gonna do? 1) Get my own Geolocation 2) Get a victim Geolocation.\n-> "))
                objMain.geolocation(option)
                if "Get Geolocation" not in logs:
                    logs.append("Get Geolocation") 
            elif opc == 4:
                print("Introduce range of ports: ")
                first_port = int(input("Initial port-> "))
                last_port = int(input("Last port -> "))
                ipaddr = input("Victim IP -> ")
                for i in range(first_port,last_port):
                    objMain.scPorts(i,ipaddr)
                
                if "Scan multiple Ports" not in logs:
                    logs.append("Scan multiple Ports")
                

            elif opc == 5:
                one_port = int(input("port-> "))
                ipaddr = input("Victim IP -> ")
                objMain.scPorts(one_port,ipaddr)
                if "Scan  a Single Ports" not in logs:
                    logs.append("Scan a Single Ports")


            elif opc == 6:
                ip_opc = input("Introduce a IP address or just introduce 127.0.0.1 if you want to know what is your own MAC address -> ")
                objMain.get_MAC(ip=ip_opc)
                if "Get MAC Address" not in logs:
                    logs.append("Get MAC Address")

            elif opc == 7:
                net = input("Introduce the network with the CDIR (192.168.3.0/24) -> ")
                objMain.getOSInfo(net)
                if "Get OS from LAN devices" not in logs:
                    logs.append("Get OS from LAN devices")
                
            elif opc == 8:
                 net = input("Introduce the network with the CDIR (192.168.3.0/24) -> ")
                 objMain.getHostnameInfo(net)
                 if "Get Hostname from LAN devices" not in logs:
                    logs.append("Get Hostname from LAN devices")

            elif opc == 9:
                objMain.getInterfaces()
                if "Get network interfaces" not in logs:
                    logs.append("Get network interfaces")

            elif opc == 10:
                objMain.sendSecretM()
                
                if "Send encrypted mail" not in logs:
                    logs.append("Send encrypted mail")

            if objMain.quit():
                with open("reporteFinal.txt","w") as reportF:
                    reportF.write('''
   _____  __    __   __    _____     __        __ __      _____  __ __     _____     __ __     _______   
 /\_____\/\_\  /_/\ /\_\  /\___/\   /\_\      /_/\__/\  /\_____\/_/\__/\  ) ___ (   /_/\__/\ /\_______)\ 
( (  ___/\/_/  ) ) \ ( ( / / _ \ \ ( ( (      ) ) ) ) )( (_____/) ) ) ) )/ /\_/\ \  ) ) ) ) )\(___  __\/ 
 \ \ \_   /\_\/_/   \ \_\\ \(_)/ /  \ \_\    /_/ /_/_/  \ \__\ /_/ /_/ // /_/ (_\ \/_/ /_/_/   / / /     
 / / /_\ / / /\ \ \   / // / _ \ \  / / /__  \ \ \ \ \  / /__/_\ \ \_\/ \ \ )_/ / /\ \ \ \ \  ( ( (      
/ /____/( (_(  )_) \ (_(( (_( )_) )( (_____(  )_) ) \ \( (_____\)_) )    \ \/_\/ /  )_) ) \ \  \ \ \     
\/_/     \/_/  \_\/ \/_/ \/_/ \_\/  \/_____/  \_\/ \_\/ \/_____/\_\/      )_____(   \_\/ \_\/  /_/_/ 

''')                
                    reportF.write("Logs fuctions used:\n")
                    for i in logs:
                        msg = f"[+] {i}\n"
                        reportF.write(msg)
                        
                print("bye.")
                break
            time.sleep(3)


        
    except:
        print("")
        