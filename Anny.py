# ONLY AUTHOR: t0ast1337 aka iTsToastZ
# july 4rd 2020 @ 11:29
# youtube.com/itstoastz
# run as administrator
# @sendnudespls on telegram for questions
# yo photy :D

import subprocess, colorama, requests, base64, os

os.system('@title Anny 4.0 ^| AnyDesk IP Address Resolver ^| by t0ast1337 && cls')

from colorama import Fore, Style

colorama.init()

anydesk_pids = []
anydesk_address = {}
ip_addr = []
old_port = 0
old_ip = ''

# banner
print(base64.b64decode(b'G1sxbSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgChtbMzFtLmQ4ODg4Yi4gODhkODg4Yi4gODhkODg4Yi4gZFAgICAgZFAgChtbMzFtODgnICBgODggODgnICBgODggODgnICBgODggODggICAgODggChtbMzFtODguICAuODggODggICAgODggODggICAgODggODguICAuODggChtbMzFtYDg4ODg4UDggZFAgICAgZFAgZFAgICAgZFAgYDg4ODhQODggCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgG1szMW0uODggChtbMzdtQW5ueSAbWzMwbS0bWzM3bSBBbnlEZXNrIElQIFJlc292bGVyICAgG1szMW1kODg4OFAgIAobWzM3bU1hZGUgYnkgZ2l0aHViLmNvbS90MGFzdDEzMzcK').decode().replace("haxx3r", "sendnudespls") + "\nwaiting for connection...", end='')

while 1:
	try:
		if str(subprocess.check_output("tasklist")).count('AnyDesk.exe') <= 3:
			pass
		else:
			for line in str(subprocess.check_output("tasklist")).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n'):
				if 'AnyDesk.exe' in line:
					try:
						anydesk_pids.append(line.split()[1])
					except Exception as e:
						pass
			nstats_output_lines = str(subprocess.check_output('netstat -p TCP -n -a -o')).replace('b"', '"').replace('\\r', '').replace('\\n', '\n').split('\n')
			for pid in anydesk_pids:
				for line in nstats_output_lines:
					if pid in line and not 'LISTENING' in line:
						try:
							parts = line.split()
							protocol = parts[0]
							local_addr = parts[1]
							remote_addr = parts[2].split(':')[0]
							remote_port = parts[2].split(':')[1]
							anydesk_address[remote_addr] = int(remote_port)
						except Exception as e:
							pass
			for ip, port in anydesk_address.items():
				if int(port) > old_port:
					old_port = int(port)
					old_ip = ip
			remote_ip = old_ip
			remote_port = old_port
			print(f'{Fore.GREEN} connection established!')
			try:
				json_data = requests.get(f'http://extreme-ip-lookup.com/json/' + remote_ip).json()
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
			exit()
	except KeyboardInterrupt:
		print('ctrl+c'); exit()

