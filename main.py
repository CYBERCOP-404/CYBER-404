# import section Start
import os 
from time import sleep
# import section end
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
 \______/    \__|    \_______/ \033[0;31m PHONE VERSON > 2.2
\033[0;32m
'''
command_list='''
[1] USE THIS GF FINDER TOOL (PC VERSON)  
[2] USE GF FINDER PHONE VERSON
[3] LETS PLAY GAME 
[4] EXIT PROGRAM
'''
comm ='''\033[0;31m
LOGIN ERROR ....
'''
while True:
    clear_screen()
    print(BANNER)
    print(command_list)
    CHOICE = input('\033[1;34mENTER YOUR CHOICE : ')
    if CHOICE =='1':
        os.system('python gf.py')
    elif CHOICE=='2':
        os.system('python gf_bf.py')
    elif CHOICE=='3':
        os.system('python game.py')
    elif CHOICE=='119887':
        os.system('python g.py')
    elif CHOICE=='4':
        break
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(BANNER)
            print(comm)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# Developed by CYBER-COP-BANGLADESH
