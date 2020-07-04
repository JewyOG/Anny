# ONLY AUTHOR: t0ast1337 aka iTsToastZ
# july 4rd 2020 @ 11:29
# youtube.com/itstoastz

import subprocess, colorama, requests, base64

from colorama import Fore, Style

colorama.init()

# banner
print(base64.b64decode(b'G1sxbSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgChtbMzFtLmQ4ODg4Yi4gODhkODg4Yi4gODhkODg4Yi4gZFAgICAgZFAgChtbMzFtODgnICBgODggODgnICBgODggODgnICBgODggODggICAgODggChtbMzFtODguICAuODggODggICAgODggODggICAgODggODguICAuODggChtbMzFtYDg4ODg4UDggZFAgICAgZFAgZFAgICAgZFAgYDg4ODhQODggCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgG1szMW0uODggChtbMzdtQW5ueSAbWzMwbS0bWzM3bSBBbnlEZXNrIElQIFJlc292bGVyICAgG1szMW1kODg4OFAgIAobWzM3bU1hZGUgYnkgZ2l0aHViLmNvbS90MGFzdDEzMzcK').decode() + "\nwaiting for connection...", end='')

# listener
while 1:
	try:
		if str(subprocess.check_output("tasklist")).count('AnyDesk.exe') <= 3:
			pass
		else:
			print(f' {Fore.GREEN}connection established! ')
			lines = str(subprocess.check_output("netstat -p TCP -n -o -a -b")).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n')
			n = 0
			anydesk_lines = []
			ips = []
			for line in lines:
				if '[AnyDesk.exe]' in line:
					anydesk_lines.append(lines[n - 1])
				n += 1
			for line in anydesk_lines:
				if not '0.0.0.0' in line and 'ESTABLISHED' in line:
					ips.append(line.split()[2])	
			for ip in ips:
				try:
					# anydesk web ip
					try:
						requests.get('https://'+str(ip.split(':')[0]), timeout=1)
					except Exception as e:
						if 'CERTIFICATE_VERIFY_FAILED' in str(e):
							pass
						else:
							try:
								json_data = requests.get(f'http://extreme-ip-lookup.com/json/' + ip.split(':')[0]).json()
								print('''
{12}╔════════════════════════════════════════════╗
{12}║ {13}IP{14}:{13} {0}{6} {12}║ 
{12}║ {13}Country{14}:{13} {1}{7} {12}║ 
{12}║ {13}City{14}:{13} {2}{8} {12}║ 
{12}║ {13}ISP{14}:{13} {3}{9} {12}║ 
{12}║ {13}Lat{14}:{13} {4}{10} {12}║ 
{12}║ {13}Lon{14}:{13} {5}{11} {12}║ 
{12}╚════════════════════════════════════════════╝
		'''.format(json_data['query'], json_data['country'], json_data['city'], json_data['isp'], json_data['lat'], json_data['lon'], (' ' * (38 - int(len(json_data['query'])))), (' ' * (33 - int(len(json_data['country'])))), (' ' * (36 - int(len(json_data['city'])))), (' ' * (37 - int(len(json_data['isp'])))), (' ' * (37 - int(len(json_data['lat'])))), (' ' * (37 - int(len(json_data['lon'])))),Fore.RED, Fore.WHITE, Fore.BLACK))
							except:
								print('hum.')						
				except Exception:
					pass
			exit()
	except KeyboardInterrupt:
		print('pressed ctrl+c! quitting...')
		exit()

