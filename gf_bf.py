BANNER = '''\033[0;32m
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\ 
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | 
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |  
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |  
 \______/    \__|    \_______/ \033[0;31m PHONE VERSON > 3.1
\033[0;32m
 [1] DO YOU NEED ANY GIRL FRIEND 
 [2] DO YOU NEED MANY GIRL FRIEND  
 [3] DO YOU WANT TO EXIT 
'''
facebook ="https://www.facebook.com/@cybercopbangladesh"
youtube = "https://www.youtube.com/@cybercopbangladesh"
github = "https://www.github.com/cybercop-404"
telegram = "t.me/cybercopbangladesh"
comm='''
Login error.........
'''
# girl section start 
sonia   = 'https://www.facebook.com/profile.php?id=61555730134982'
sadia   = 'https://www.facebook.com/profile.php?id=61550780090307'
nusrat  = 'https://www.facebook.com/profile.php?id=61559358894560'
rani    = 'https://www.facebook.com/nilaaktar.nilisha'
maisa   = 'https://www.facebook.com/misha.moon1'
nusu    = 'https://www.facebook.com/profile.php?id=61558430423969'
mahiya  = 'https://www.facebook.com/profile.php?id=61557292204247'
sanjida = 'https://www.facebook.com/profile.php?id=100092753300663'
raisa   = 'https://www.facebook.com/profile.php?id=61552388255134'
israt   = 'https://www.facebook.com/profile.php?id=61554654218911'
dipika  = 'https://www.facebook.com/profile.php?id=61554460332896'
joba    = 'https://www.facebook.com/profile.php?id=61555692063422'
shuli   = 'https://www.facebook.com/profile.php?id=100091079419380'
sagorika= 'https://www.facebook.com/profile.php?id=61559189518344'
mim     = 'https://www.facebook.com/profile.php?id=61559610456576'
khalifa = 'https://www.facebook.com/miakhalifa'
urmi    = 'https://www.facebook.com/profile.php?id=100089930927342'
tuli    = 'https://www.facebook.com/profile.php?id=100095012946033'
suraiya = 'https://www.facebook.com/profile.php?id=100093698431143'
rubi    = 'https://www.facebook.com/profile.php?id=100057352509405'
runa    = 'https://www.facebook.com/profile.php?id=61559437694078'
merin   = 'https://www.facebook.com/profile.php?id=61556344526956' 

# girl section end 
girl_list =[sonia,sadia,nusrat,rani,maisa,nusu,mahiya,sanjida,raisa,israt,dipika,joba,shuli,sagorika,mim,tuli,suraiya,rubi,runa,merin]
# import section start.  
from random2 import choice
from time import sleep
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
	clear_screen()
	MAME = input('WHAT IS YOUR NAME : ')
	NAME = MAME.upper()
	clear_screen()
	print('FOLLOW MY ALL ID .........')
	sleep(2)
	os.system(f'xdg-open {youtube}')
	sleep(4)
	os.system(f'xdg-open {github}')
	sleep(4)
	os.system(f"xdg-open {facebook}")
	sleep(4)
	clear_screen()
	print(BANNER)
	ino = input('WHAT IS YOUR CHOICE : ')
	if ino =='1':
			ok = choice(girl_list)
			print('Congratulation......  YOU HAVE NOW GIRLFRIEND ')
			os.system(f'xdg-open {ok}')
	elif ino =='2':
			print('FUCK YOU......  YOU ARE FUCK BOY........ THATS WHY YOU ARE SINGLE......  FUCK YOU  '+NAME)
			INPUTO = input('DO YOU WANT TO EXIT..... PRESS ENTER')
			if INPUTO =='1':
				print('HELLO CYBER-COP')
			else:
				break
	elif ino =='3':
		print('FOLLOW MY ALL ID ......')
		sleep(2)
		os.system(f'xdg-open {youtube}')
		sleep(4)
		os.system(f'xdg-open {github}')
		sleep(4)
		os.system(f"xdg-open {facebook}")
		break
# Developer CYBER-COP
