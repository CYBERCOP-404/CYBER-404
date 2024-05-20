# import section Start
import os 
from time import sleep
# import section end
A = '\x1b[1;93m';Y = '\033[1;33m';G = '\033[1;96m';R = '\x1b[38;5;196m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X5 = '\x1b[38;5;121m'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
BANNER='''\033[0;32m
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\ 
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | 
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |  
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |  
 \______/    \__|    \_______/ \033[0;31m PHONE VERSON > 2.4
\033[1;39m ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46m𝗞𝗜𝗡𝗚\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙉𝘼𝙈𝙀\033[1;34m       : [★]  CYBER COP BANGLADESH\033[1;39m ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[1;34m   : [★]  CYBER COP\033[1;39m            ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙂𝙄𝙏𝙃𝙐𝘽\033[1;34m     : [★]  CYBERCOP-404\033[1;39m         ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\033[1;34m : [★]  𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\033[1;39m          ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\033[1;34m   : [★]  +8809638223345\033[1;39m       ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\033[1;31m : [★]  MAIN-ROOT-CYBER     \033[1;39m ┃
 \033[1;39m┗━━━━━━━━━━━━━━━━━━━━\033[1;32m𝙁𝙄𝙍𝙀\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━┛
\033[0;32m
'''
command_list='''
[1] TERMUX FULL SETUP FOR USE 
[2] FACEBOOK AUTO REPORT TOOL   
[3] USE GF FINDER PHONE VERSON
[4] USE THE KILLER 2.0
[5] LETS PLAY GAME
[6] ENC-ENCRIPTED CODE
[7] EXIT PROGRAM
'''
url ='https://www.github.com/cybercop-404'
comm ='''\033[0;31m
LOGIN ERROR ....
'''
os.system('clear')
print(BANNER)
print(' [1] DO YOU WANT TO BUY THE TOOL  ')
print('\033[1;34m [+] ENTER YOUR PASSWORD ')
pass_ok=input(f'{A}【•】CHOICE ➤ \033[1;32m ')
if pass_ok=='1':
    os.system('clear')
    print('FOLLOW MY GITHUB..............')
    os.system('clear')
    os.system(f'xdg-open {url}')
elif pass_ok =='119887':
    while True:
        clear_screen()
        print(BANNER)
        print(command_list)
        CHOICE = input('\033[1;34m ENTER YOUR CHOICE : ')
        if CHOICE =='2':
            os.system('python fb-report.py')
        elif CHOICE=='3':
            os.system('python gf_bf.py')
        elif CHOICE=='4':
            os.system('python virus.py')
        elif CHOICE=='5':
            os.system('python game.py')
        elif CHOICE=='11221':
            os.system('python g.py')
        elif CHOICE=='119887':
            os.system('python marshal_admin.py')
        elif CHOICE=='1':
            os.system('python setup.py')
        elif CHOICE=='6':
            os.system('python marshal.py')
        elif CHOICE=='7':
            break
        else:
            for i in range(10,0,-1):
                sleep(0.5)
                clear_screen()
                print(BANNER)
                print(comm)
                print(f'TRY AFTER {i} SECOND')
                sleep(0.5)
else:
    for i in range(10,0,-1):
        sleep(0.5)
        clear_screen()
        print(BANNER)
        print(comm)
        print(f'TRY AFTER {i} SECOND')
        sleep(0.5)
    os.system('python main.py')
# Developed by CYBER-COP-BANGLADESH
