import requests
import json
import time
import os,sys
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

print(Fore.GREEN + "             )                               ") 
print(Fore.GREEN + "     (    ( /(       (    (           )      ") 
print(Fore.GREEN + " (   )\   )\())   )  )\ ) )\ )   ) ( /(    ) ") 
print(Fore.GREEN + " )\ ((_) ((_)\ ( /( (()/((()/(( /( )\())( /( ") 
print(Fore.GREEN + "((_) _    _((_))(_)) ((_))((_))(_)|(_)\ )(_))") 
print(Fore.GREEN + "| __| |  | \| ((_)_  _| | _| ((_)_| |(_|(_)_ ") 
print(Fore.GREEN + "| _|| |  | .` / _` / _` / _` / _` | ' \/ _` |")
print(Fore.GREEN + "|___|_|  |_|\_\__,_\__,_\__,_\__,_|_||_\__,_|")
print(Fore.GREEN + "")




try:
    urlapifile = open('urlapi.txt','r')
    urlapi = urlapifile.readline().strip('\n')
    print('[+] API in use : '+urlapi.strip('\n'))
except:
    print(Fore.RED + "[+] Error : Couldn't find urlapi.txt file.")
    print("[+] Usage : python.exe naddaha.py <list_file> ")
    sys.exit()


if len(sys.argv) <= 1:
    print(Fore.RED + "[+] Error : Couldn't find input file .")
    print("[+] Usage : python.exe naddaha.py <list_file> ")
    sys.exit()    
else :    
    fileurlcheck = sys.argv[1]
    
print("[+] Checking file : "+sys.argv[1])
headers = {'API-Key':urlapi,'Content-Type':'application/json'}
try:
    urlfileopen = open(fileurlcheck, 'r')
except:
    print(Fore.RED + "[+] Error : Issue opening the file : " +fileurlcheck+" .")
    sys.exit()
    

urlLines = urlfileopen.readlines()

for urls in urlLines:    
    data = {"url": urls , "visibility": "private"}
    try:
        print("[+] Checking url : "+urls)
        response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
        if response.status_code == 400:
                print ("[+] Output : "+response.json()['message'])
        urlimage = response.json()['result']
        urluuid = response.json()['uuid']
        print ("[+] Output : "+response.json()['message'])
        print ("[+] Urlscan : "+response.json()['result'])
        print ("[+] Visibility : "+response.json()['visibility'])
        print("[+] Downloading the image ...")
        time.sleep(25)
        try:
            responseimg = requests.get('https://urlscan.io/screenshots/'+urluuid+'.png')
            print ("[+] Image code : "+ str(responseimg.status_code))
            print ('[+] https://urlscan.io/screenshots/'+urluuid+'.png')
            if responseimg.status_code == 200:
                with open(urluuid+".png", 'wb') as f:
                    f.write(responseimg.content)
                print("Image name : "+urluuid+".png")
        except:
            print (Fore.RED + "[!] ERROR : issue took place while downloading the image.")
    except:
            print (Fore.RED + "[!] Oops!!")
            
    print("="*60)