import os
from time import sleep
from random import choice
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
BANNER ='''\033[1;31m
  _  _______ _      _      ______ _____  
 | |/ /_   _| |    | |    |  ____|  __ \ 
 | ' /  | | | |    | |    | |__  | |__) |
 |  <   | | | |    | |    |  __| |  _  / 
 | . \ _| |_| |____| |____| |____| | \ \ 
 |_|\_\_____|______|______|______|_|  \_\Verson 2.0 
'''
ADMIN_LIST ='''
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
url ="https://www.github.com/cybercop-404"
f='''\033[1;31m
THIS TOOL CAN KILL YOUR DEVICE .......
'''
COMMAND='''\033[1;31m
[1] I WANT TO RUN THIS TOOL\033[1;39m
[2] I WANT TO EXIT THE TOOL
'''
def animate_text(text):
    [print(char, end='', flush=True) or sleep(0.004) for char in text]
    print()
file_count = 0
numbe =[]
for i in range(0,99999):
    numbe.append(i)
os.system('clear')
animate_text(d)
sleep(3)
os.system('clear')
animate_text(f)
sleep(3)
os.system('mkdir VIRUS')
os.chdir('VIRUS')
os.system('clear')
print('FOLLOW MY GITHUB .......')
sleep(2)
os.system(f'xdg-open {url}')
sleep(5)
os.system('clear')
animate_text(BANNER)
animate_text(ADMIN_LIST)
animate_text(COMMAND)
want =int(input('WHAT DO YOU WANT : '))
if want ==1:
    while True:
        c = choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
        q=choice(numbe)
        os.system(f'mkdir CYBER-COP-VIRUS{q}')
        file_count += 1
        print(f'{c}[{file_count}] CREATED FILE SUCCESSFULL...')
elif want ==2:
    breakpoint
else:
    breakpoint
# Developer CYBER-COP-BANGLADESH
