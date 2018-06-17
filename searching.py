#!/usr/bin/env python3
# Criador: Matheus Santana
# Canal: Hae Brasil / System21
# Team: [HAE]Hazardous Hacking 
# (Hae Brasil) https://www.youtube.com/c/haebrasil     
# (Cientistas da Tecnologia) https://www.youtube.com/channel/UCFYwt_Wz1VHpqVb2mFxg8aA
import requests
import os
from urllib.parse import urlparse, urlunparse

os.system('clear') 
if os.sys.platform == 'windows': 
    print("Not available for this system.")
print ("""\033[1;33m   ____                 __   _          
  / __/__ ___ _________/ /  (_)__  ___ _
 _\ \/ -_) _ `/ __/ __/ _ \/ / _ \/ _ `/
/___/\__/\_,_/_/  \__/_//_/_/_//_/\_, / 
                                 /___/  \033[0;0m""")
print('\033[1;32mv.1.0\033[0;0m')
print('\033[32mCreator: Matheus Santana\033[0;0m')
print('\033[32mChannel: https://goo.gl/tjKAHQ\033[0;0m')
print('-'*45)
print('\033[32mEx: 172.217.29.68 or www.google.com\033[0;0m')
print('-'*45)
try:
    url=str(input('\033[33mInsert the link: \033[0;0m'))
    print('-'*45)
    if url[-1:] != '/':
	    url += '/'
    def cnx(url):
        if ":" not in url:
             url = "http://" + url
        parsed = list(urlparse(url, scheme='https'))
        parsed[0] = 'http'
        return urlunparse(parsed)
    url = cnx(url) 
    arq = open('wordlist.txt')
    print("\033[33m\nLooking for admin panel...\n\033[0;0m")
    for xy in arq.read().split():
        x = requests.get(url + xy)
        if x.status_code == 200:
            print('\033[33mFound: \033[0;0m',url + xy) 
    arq2 = open('wordlist2.txt')
    print('\033[33m\nSearching for files and directories...\n\033[0;0m')
    for x in arq2.read().split():
        y = requests.get(url + x)
        if y.status_code == 200 or y.status_code == 403:
            print('\033[33mFound: \033[0;0m',url + x)
except KeyboardInterrupt as erro:
    print('\n\033[1;31;40mInterrompido!\033[0;0m')
