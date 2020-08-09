import requests
import argparse
from time import ctime , time 
import os
from multiprocessing import Pool
r = '\033[31m'
g = '\033[32m' 
y = '\033[33m' 
b = '\033[34m' 
m = '\033[35m' 
c = '\033[36m' 
w = '\033[37m'
printf = ("""

db   d8b   db d8888b.        d8888b. d8888b.        d88888b db    db 
88   I8I   88 88  `8D        88  `8D 88  `8D        88'     `8b  d8' 
88   I8I   88 88oodD'        88   88 88oooY'        88ooooo  `8bd8'  
Y8   I8I   88 88~~~   C8888D 88   88 88~~~b. C8888D 88~~~~~  .dPYb.  
`8b d8'8b d8' 88             88  .8D 88   8D        88.     .8P  Y8. 
 `8b8' `8d8'  88             Y8888D' Y8888P'        Y88888P YP    YP 
                        
                """+w+" < Alert > Tested BY : SalimAlk "+r+"""  
                         Parrot Os            
"""+w)
parser = argparse.ArgumentParser()
t = time()
parser.add_argument("-u", "--url", help="List Sites")
cmd = parser.parse_args()
target = cmd.url
wned = g+"| [+] Server : "+w
Started = g+"| [+] Started in : "+w+ctime(t)
job = g+"| [+] Find DB-Ex "+":"+w+" Working "
timeout = g+"| [+] TimeOut "+w+": 10s "
Author = g+"| [+] Author  "+w+": Salim Alk" 
def pf():
	print Started
	print job
	print timeout
	print Author
def serv():
	try:
		try:
			try:
				srv = requests.get(target, timeout=10)
				server = (srv.headers['Server'])
				print ('{}'+server).format(wned)
			except KeyboardInterrupt:
				print(" Exit __________________>")
				exit()
		except requests.exceptions.MissingSchema:
			print (" Can't Connect Host Add http:// to URL ")
	except requests.exceptions.ReadTimeout:
		print(w+target+g+' Timeout ')
def searching(dirc):
	try:
		hostage = target+"/"+dirc
		Squezy = requests.get(hostage, allow_redirects=False)
		if Squezy.status_code==200:
			print(r+" [+] Dumped : "+w+hostage)
			with open("rezlt/db-dirc.txt", "w") as f:
				f.write('\n'+hostage)
		else:
			print(r+" [+] No : "+w+hostage)
	except KeyboardInterrupt:
		exit()
def all():
	os.system("clear")
	#time.sleep(4)
	print(printf)
	pf()
	serv()
all()
try:
	TEXTList = open('db.txt', 'r').read().splitlines()
	p = Pool(1)
	p.map(searching, TEXTList)
except KeyboardInterrupt:
	exit()
			for i in op:
				for i in i.split():
					hostage = target+"/"+i
					Squezy = requests.get(hostage, allow_redirects=False)
					if Squezy.status_code==200:
						print(r+" [+] Dumped : "+w+hostage)
						with open("rezlt/db-dirc.txt", "w") as f:
							f.write('\n'+hostage)
					else:
						pass
		except KeyboardInterrupt:
			print(" Can't Exist Beacuse Multi ")
			exit()
	except requests.exceptions.MissingSchema:
		exit()
def multi():
	try:
		TEXTList = open('db.txt', 'r').read().splitlines()
		p = Pool(5)
		p.map(searching, TEXTList)
	except KeyboardInterrupt:
		exit()
def all():
	os.system("clear")
	#time.sleep(4)
	print(printf)
	pf()
	serv()
	multi()
all()
