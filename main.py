# import section Start
import os 
from time import sleep
# import section end
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
BANNER='''\033[1;32m
  /$$$$$$  /$$     /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$           /$$$$$$   /$$$$$$  /$$$$$$$ 
 /$$__  $$|  $$   /$$/| $$__  $$| $$_____/| $$__  $$         /$$__  $$ /$$__  $$| $$__  $$
| $$  \__/ \  $$ /$$/ | $$  \ $$| $$      | $$  \ $$        | $$  \__/| $$  \ $$| $$  \ $$
| $$        \  $$$$/  | $$$$$$$ | $$$$$   | $$$$$$$/ /$$$$$$| $$      | $$  | $$| $$$$$$$/
| $$         \  $$/   | $$__  $$| $$__/   | $$__  $$|______/| $$      | $$  | $$| $$____/ 
| $$    $$    | $$    | $$  \ $$| $$      | $$  \ $$        | $$    $$| $$  | $$| $$      
|  $$$$$$/    | $$    | $$$$$$$/| $$$$$$$$| $$  | $$        |  $$$$$$/|  $$$$$$/| $$      
 \______/     |__/    |_______/ |________/|__/  |__/         \______/  \______/ |__/   Verson-2.1
'''
command_list='''
[1] USE THIS GF FINDER TOOL  
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
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(BANNER)
            print(comm)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# Developed by CYBER-COP-BANGLADESH
