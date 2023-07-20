import psutil
class Interface:
    def get_status(self):
        status = psutil.net_if_stats()
        print("[-]Interfaces:")
        for key, value in status.items():
            print(f"\t[+]{key}",end="")
            if "True" in str(value):
                print(" [UP].")
            elif "False" in str(value):
                print(" [DOWN].")