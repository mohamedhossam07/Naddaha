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



urlapifile = open('urlapi.txt','r')
try:
    urlapi = urlapifile.readline()
except:
    print("[+] Error : Couldn't find urlapi.txt file.")

try:
    fileurlcheck = sys.argv[1]
except:
    print("[+] Usage : python.exe urlscanner.py <list_file> ")
    sys.exit()
print("- Checking file : "+sys.argv[1])
headers = {'API-Key':urlapi,'Content-Type':'application/json'}
try:
    urlfileopen = open(fileurlcheck, 'r')
except:
    print("[+] Error : Issue opening the file : " +fileurlcheck+" .")
    sys.exit()
    

urlLines = urlfileopen.readlines()

for urls in urlLines:    
    data = {"url": urls , "visibility": "private"}
    try:
        print("[+] Checking url : "+urls)
        response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
        if response.status_code == 400:
                print ("- Output : "+response.json()['message'])
        urlimage = response.json()['result']
        urluuid = response.json()['uuid']
        print ("- Output : "+response.json()['message'])
        print ("- Urlscan : "+response.json()['result'])
        print ("- Visibility : "+response.json()['visibility'])
        print("- Downloading the image ...")
        time.sleep(25)
        try:
            responseimg = requests.get('https://urlscan.io/screenshots/'+urluuid+'.png')
            print ("- Image code : "+ str(responseimg.status_code))
            print ('- https://urlscan.io/screenshots/'+urluuid+'.png')
            if responseimg.status_code == 200:
                with open(urluuid+".png", 'wb') as f:
                    f.write(responseimg.content)
                print("Image name : "+urluuid+".png")
        except:
            print ("ERROR!")
    except:
            print ("Oops!!")
            
    print("="*60)