banner='''
\033[0;32m
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\ 
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | 
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |  
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |  
 \______/    \__|    \_______/ \033[0;31m PHONE VERSON > 2.3
\033[0;32m
'''
list_k ='''
[1] START GAME
[2] EXIT PROGRAM
'''
#  all link 
github = 'https://www.github.com/cybercop-404/'
TELEGRAM = "https://t.me/cybercopbangladesh"
# import section start .
from random2 import choice
from time import sleep
import os
# import section end 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
name_list =[]
while True:
    clear_screen()
    print("FOLLOW MY ALL ID AND JOIN GROUP")
    os.system(f'xdg-open {TELEGRAM}')
    clear_screen()
    print(banner)
    print(list_k)
    user = input('WHAT IS YOUR CHOICE : ')
    if user =='1':
        print('WHEN YOUR TEXT IS OVER WRIGHT RUN PRESS ENTER')
        sleep(5)
        while True:
            clear_screen()
            print(banner)
            namo = input('ENTER YOUR TEXT : ')
            name =namo.upper()
            if name =='RUN':
                output = choice(name_list)
                print('\033[0;31mCONGRATULATION ........' + output +' YOU ARE THE WINNER ! ')
                sleep(10)
                os.system(f'xdg-open {github}')
            else:
                name_list.append(name)
    elif user =='2':
        break
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(banner)
            print('\033[0;31mLogin error .........')
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
print('FOLLOW MY GITHUB ')
sleep(2)
os.system(f'xdg-open {github}')
# developer CYBER-COP-BANGLADESH
