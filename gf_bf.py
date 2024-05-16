BANNER = '''\033[0;32m
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\ 
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | 
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |  
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |  
 \______/    \__|    \_______/ \033[0;31m PHONE VERSON > 2.2
\033[0;32m
 [1] DO YOU NEED ANY GIRL FRIEND 
 [2] DO YOU NEED MANY GIRL FRIEND  
 [3] DO YOU WANT TO EXIT 
'''
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
# girl section end 
girl_list =[sonia,sadia,nusrat,rani,maisa,nusu,mahiya,sanjida,raisa,israt]
# import section start.  
from random2 import choice
from time import sleep
while True:
	print(BANNER)
	MAME = input('WHAT IS YOUR NAME : ')
	NAME = MAME.upper()
	ino = input('WHAT IS YOUR CHOICE : ')
	if ino =='1':
			ok = choice(girl_list)
			print('Congratulation......  You have now girl friend > ')
			print(ok)
			print()
			print()
			exit = input('DO YOU WANT TO EXIT NOW ?  PRESS ENTER')
			if exit =='1':
				print('HELLO  CYBER-COP')
			else:
				break
	elif ino =='2':
			print('FUCK YOU......  YOU ARE FUCK BOY........ THATS WHY YOU ARE SINGLE......  FUCK YOU  '+NAME)
			INPUTO = input('DO YOU WANT TO EXIT..... PRESS ENTER')
			if INPUTO =='1':
				print('HELLO CYBER-COP')
			else:
				break
	elif ino =='3':
		break
# Developer CYBER-COP
