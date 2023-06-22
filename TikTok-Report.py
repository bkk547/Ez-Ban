import time
from datetime import datetime
from colorama import *
import requests
from requests.sessions import session


print(Fore.RED + '''
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗   ██████╗  █████╗ ███╗   ██╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝   ██╔══██╗██╔══██╗████╗  ██║
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝    ██████╔╝███████║██╔██╗ ██║
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗    ██╔══██╗██╔══██║██║╚██╗██║
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗██╗██████╔╝██║  ██║██║ ╚████║
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                                         GitHub: LeetIDA                                  
''')




tiktok_url = input("Request Link: ")

while True:

    proxies = requests.get(url="https://advanced.name/freeproxy/6494b892c8fa8").text.split('\r\n') #Update Your Proxy List From This URL (https://advanced.name/freeproxy/)

    for proxy in proxies:

        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            req = session().post(tiktok_url, proxies={'http': f'http://{proxy}'})

            print(Fore.RED + f'[{current_time}]' + Fore.GREEN + f' Proxy: {proxy} Report Sent')
        except:
            print(Fore.RED +'Some Thing Gay Here Its Not Working :) ')
            input('Press Enter to close the program')
            exit()
