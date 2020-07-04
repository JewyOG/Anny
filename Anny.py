# ONLY AUTHOR: t0ast1337 aka iTsToastZ
# july 3rd 2020
# youtube.com/itstoastz
# NOTE: THERE IS A LITTLE BUG WHO ILL FIX LATER SO DONT DL IT RN

import subprocess
import colorama
import requests
import sys

from colorama import *

colorama.init()

def locate(ip):
	json_data = requests.get(f'http://extreme-ip-lookup.com/json/{ip}').json()
	print(Fore.RED + Style.DIM + '''╔════════════════════════════════════════════╗
''' + Fore.RED + Style.DIM + '''║ ''' + Fore.WHITE + Style.BRIGHT + '''IP''' + Fore.BLACK + ''':''' + Fore.WHITE+ ''' ''' + json_data['query'] + (' ' * (38 - int(len(json_data['query'])))) + Fore.RED + Style.DIM + ''' ║
''' + Fore.RED + Style.DIM + '''║ ''' + Fore.WHITE + Style.BRIGHT + '''Country''' + Fore.BLACK + ''':''' + Fore.WHITE+ ''' ''' + json_data['country'] + (' ' * (33 - int(len(json_data['country'])))) + Fore.RED + Style.DIM + ''' ║
''' + Fore.RED + Style.DIM + '''║ ''' + Fore.WHITE + Style.BRIGHT + '''City''' + Fore.BLACK + ''':''' + Fore.WHITE+ ''' ''' + json_data['city'] + (' ' * (36 - int(len(json_data['city'])))) + Fore.RED + Style.DIM + ''' ║
''' + Fore.RED + Style.DIM + '''║ ''' + Fore.WHITE + Style.BRIGHT + '''ISP''' + Fore.BLACK + ''':''' + Fore.WHITE+ ''' ''' + json_data['isp'] + (' ' * (37 - int(len(json_data['isp'])))) + Fore.RED + Style.DIM + ''' ║
''' + Fore.RED + Style.DIM + '''║ ''' + Fore.WHITE + Style.BRIGHT + '''Lat''' + Fore.BLACK + ''':''' + Fore.WHITE+ ''' ''' + json_data['lat'] + (' ' * (37 - int(len(json_data['lat'])))) + Fore.RED + Style.DIM + ''' ║
''' + Fore.RED + Style.DIM + '''║ ''' + Fore.WHITE + Style.BRIGHT + '''Lon''' + Fore.BLACK + ''':''' + Fore.WHITE+ ''' ''' + json_data['lon'] + (' ' * (37 - int(len(json_data['lon'])))) + Fore.RED + Style.DIM + ''' ║
''' + Fore.RED + Style.DIM + '''╚════════════════════════════════════════════╝''')


banner = f'''                                                                       
{Fore.RED}{Style.DIM}.d8888b. 88d888b. 88d888b. dP    dP 
{Fore.RED}{Style.DIM}88'  `88 88'  `88 88'  `88 88    88 
{Fore.RED}{Style.DIM}88.  .88 88    88 88    88 88.  .88 
{Fore.RED}{Style.DIM}`88888P8 dP    dP dP    dP `8888P88 
{Fore.BLACK}{Style.BRIGHT}oooooooooooooooooooooooooooo~~~~{Fore.RED}{Style.DIM}.88{Fore.BLACK}{Style.BRIGHT}~
                            {Fore.RED}{Style.DIM}d8888P{Style.BRIGHT}  
{Fore.WHITE}AnyDesk {Fore.BLACK}{Style.BRIGHT}IP {Fore.WHITE}Resolver
{Fore.RED}{Style.DIM}youtube.com/itstoastz
github.com/t0ast1337
telegram.me/haxx3r{Fore.WHITE}{Style.BRIGHT}
'''

print(banner)
print("waiting for connection...", )
while 1:
	if str(subprocess.check_output("tasklist")).count('AnyDesk.exe') <= 3:
		pass
	else:
		lines = str(subprocess.check_output("netstat -p TCP -n -o -a -b")).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n')
		n = 0
		anydesk_lines = []
		for line in lines:
			if '[AnyDesk.exe]' in line:
				anydesk_lines.append(lines[n - 1])
			n += 1
	
		ips = []
	
		for line in anydesk_lines:
			if not '0.0.0.0' in line and 'ESTABLISHED' in line:
				parts = line.split()
				ips.append(parts[2])
	
		for _ip in ips:
			try:
				ip = _ip.split(':')[0]
				if not '136.243' in str(ip): # anydesk web ip
					locate(ip)
					exit()
			except Exception as e:
				pass

