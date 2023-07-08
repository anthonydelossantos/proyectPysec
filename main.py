import networkSniff
import websiteInfo
import geolocator
import scanPorts
import Macaddres
import hostnameInformation, osInformation,interfaces
import smtMail

class Main:
    option = 0

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
        self.printstr("Analizing Website...")
    def geolocation(self):
        self.printstr("Getting the location...")
    def scMPorts(self):
        self.printstr("Scanning Multiple Ports...")
    def scSPort(self):
        self.printstr("Scanning a Single Port...")
    def analizeTraffic(self):
        self.printstr("Getting the MAC address...")
    def getOSInfo(self):
        self.printstr("Getting all OS devices information...")
    def getHostnameInfo(self):
        self.printstr("Getting all hostname devices information...")
    def getInterfaces(self):
        self.printstr("Getting all the interfaces...")
    def sendSecretM(self):
        self.printstr("Connecting to SMTP...")


if __name__ == '__main__':
    try:
        objMain = Main()
        while True:
            objMain.menu()
            opc = int(input("Choose a number [1-10] -> "))
            objMain.set_value(opc)
            if objMain.quit():
                print("bye.")
                break


        
    except:
        print("")