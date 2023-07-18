import requests,json
class Geolocator:
    url = 'https://geolocation-db.com/jsonp/'
    ip = ""
    def set_value(self,ip=""):
        self.ip = ip
        
    def get_ownLocation(self):
        res = requests.get(self.url)
        result = res.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)
        print(f"[-]Your IP Geolocation \n[+] IP:  {result['IPv4']}")
        print(f"[+]Country: {result['country_name']}\n[+]City: {result['city']}\n[+]State: {result['state']}\n[+]Latitude: {result['latitude']}\n[+]Longituted: {result['longitude']}")
    def get_geoLocation(self,ip):
        url_2 = self.url +f"/{ip}"
        res = requests.get(url_2)
        result = res.content.decode()
        result = result.split("(")[1].strip(")")
        result = json.loads(result)
        print(f"[-]Victim IP Geolocation \n[+] IP:  {result['IPv4']}")
        print(f"[+]Country: {result['country_name']}\n[+]City: {result['city']}\n[+]State: {result['state']}\n[+]Latitude: {result['latitude']}\n[+]Longituted: {result['longitude']}")
