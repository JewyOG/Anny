# ONLY AUTHOR: t0ast1337 aka iTsToastZ
# july 3rd 2020
# youtube.com/itstoastz

import subprocess
import colorama
import requests
import socket
import struct

from colorama import *

colorama.init()

def locate(ip):
	json_data = requests.get(f'http://extreme-ip-lookup.com/json/{ip}').json()
	ip = json_data['query']
	continent = json_data['continent']
	country = json_data['country']
	region = json_data['region']
	city = json_data['city']
	isp = json_data['isp']
	lat = json_data['lat']
	lon = json_data['lon']
	space_ip = ' ' * (38 - int(len(ip)))
	space_country = ' ' * (33 - int(len(country)))
	space_city = ' ' * (36 - int(len(city)))
	space_isp = ' ' * (37 - int(len(isp)))
	space_lat = ' ' * (37 - int(len(lat)))
	space_lon = ' ' * (37 - int(len(lon)))
	message = f'''
{Style.DIM}{Fore.RED}╔════════════════════════════════════════════╗
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}IP{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}{ip}{space_ip} {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}Country{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}{country}{space_country} {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}City{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}{city}{space_city} {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}ISP{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}{isp}{space_isp} {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}Lat{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}{lat}{space_lat} {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}Lon{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}{lon}{space_lon} {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}╚════════════════════════════════════════════╝
	'''
	print(message)

banner = f'''
{Fore.RED}.s5SSSs.      .s    s.      .s    s.      .s5 s.
{Fore.RED}      SS.           SS.           SS.         SS.
{Fore.RED}sS    S%S     sSs.  S%S     sSs.  S%S     ssS SSS
{Fore.RED}SS    S%S     SS`S. S%S     SS`S. S%S     SSS SSS
{Fore.RED}SSSs. S%S     SS `S.S%S     SS `S.S%S      SSSSS
{Fore.RED}SS    S%S     SS  `sS%S     SS  `sS%S       SSS
{Fore.RED}SS    `:;     SS    `:;     SS    `:;       `:;
{Fore.RED}SS    ;,.     SS    ;,.     SS    ;,.       ;,.
{Fore.RED}:;    ;:'     :;    ;:'     :;    ;:'       ;:'

{Style.BRIGHT}{Fore.WHITE}     ANYDESK  {Style.BRIGHT}{Fore.BLACK}-  {Style.BRIGHT}{Fore.WHITE}IP  {Style.BRIGHT}{Fore.BLACK}-  {Style.BRIGHT}{Fore.WHITE}ADDRESS  {Style.BRIGHT}{Fore.BLACK}-  {Style.BRIGHT}{Fore.WHITE}RESOLVER
{Style.DIM}{Fore.RED}╔═══════════════════════════════════════════════╗
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}GitHub{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}github.com/t0ast1337                  {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}YouTube{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}youtube.com/iTsToastZ                {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}║ {Style.BRIGHT}{Fore.WHITE}Telegram{Style.BRIGHT}{Fore.BLACK}: {Style.BRIGHT}{Fore.WHITE}@haxx3r                             {Style.DIM}{Fore.RED}║
{Style.DIM}{Fore.RED}╚═══════════════════════════════════════════════╝
{Style.BRIGHT}{Fore.WHITE}
'''

print(banner)

output = subprocess.check_output("tasklist")
if output.count('AnyDesk.exe') <= 3:
	print('nobody is connected to ur session!')
	exit()

raw = ''
output = subprocess.check_output("netstat -p TCP -n -o -a -b")
output = str(output).replace('b"', '"')
output = str(output.replace('\\r', '').replace('\\n', '\n'))
lines = output.split('\n')
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
		locate(ip)
	except Exception as e:
		print(e)
