# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
import os
from time import sleep
from random import choice
from sys import stdout

# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
BANNER ='''\033[1;31m
  _  _______ _      _      ______ _____  
 | |/ /_   _| |    | |    |  ____|  __ \ 
 | ' /  | | | |    | |    | |__  | |__) |
 |  <   | | | |    | |    |  __| |  _  / 
 | . \ _| |_| |____| |____| |____| | \ \ 
 |_|\_\_____|______|______|______|_|  \_\Verson 2.0 

 \033[1;39m ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46m𝗞𝗜𝗡𝗚\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙉𝘼𝙈𝙀\033[1;34m       : [★]  CYBER COP BANGLADESH\033[1;39m ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[1;34m   : [★]  CYBER COP\033[1;39m            ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙂𝙄𝙏𝙃𝙐𝘽\033[1;34m     : [★]  CYBERCOP-404\033[1;39m         ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\033[1;34m : [★]  𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\033[1;39m          ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\033[1;34m   : [★]  +8809638223345\033[1;39m       ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\033[1;31m : [★]  FILE-AUTO-BOMBER    \033[1;39m ┃
 \033[1;39m┗━━━━━━━━━━━━━━━━━━━\033[1;32m 𝙁𝙄𝙍𝙀\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━┛
'''

d='''\033[1;31m
THIS TOOL IS VERRY DENGURUS.........
'''
f='''\033[1;31m
THIS TOOL CAN KILL YOUR DEVICE .......
'''
COMMAND='''\033[1;31m
[1] I WANT TO RUN THIS TOOL\033[1;39m
[2] I WANT TO EXIT THE TOOL
'''
R = '\033[31;1m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
# --------------------------------------[ MAIN ANNIMATION ]------------------------------------------------------------ #
animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
def animate_text(text):
    [print(char, end='', flush=True) or sleep(0.004) for char in text]
    print()
file_count = 0
# --------------------------------------[ CLEAR PROGRAM ]------------------------------------------------------------- #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# --------------------------------------[ ANIMATION PROGRAM ]---------------------------------------------------------- #
def anima(animation):
    for i in range(len(animation)):
        sleep(0.5)
        stdout.write("\r[😊] PREPARING... " + animation[i % len(animation)])
        stdout.flush()
# --------------------------------------[ URL HERE ]---------------------------------------------------------- #
url ="https://www.github.com/cybercop-404"
# --------------------------------------[ MAIN BODY ]------------------------------------------------------- #

anima(animation)
clear()
animate_text(d)
sleep(3)
clear()
animate_text(f)
sleep(3)
os.system('mkdir VIRUS')
os.chdir('VIRUS')
clear()
print('FOLLOW MY GITHUB .......')
sleep(2)
os.system(f'xdg-open {url}')
sleep(5)
clear()
file_count = 0
i=1
animate_text(BANNER)
animate_text(COMMAND)
want =int(input('WHAT DO YOU WANT : '))
if want ==1:
    while True:
        c = choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
        os.system(f'mkdir CYBER-COP-VIRUS{i}')
        file_count += 1
        i +=1
        print(f'{c}[{file_count}] CREATED FILE SUCCESSFULL...')
elif want ==2:
    breakpoint
else:
    breakpoint
# Developer CYBER-COP-BANGLADESH
