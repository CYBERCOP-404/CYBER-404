BANNERR = '''
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\           $$$$$$\   $$$$$$\  $$$$$$$\  
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\         $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ |        $$ /  \__|$$ /  $$ |$$ |  $$ |
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |$$$$$$\ $$ |      $$ |  $$ |$$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< \______|$$ |      $$ |  $$ |$$  ____/ 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |        $$ |  $$\ $$ |  $$ |$$ |      
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |        \$$$$$$  | $$$$$$  |$$ |      
 \______/    \__|    \_______/ \________|\__|  \__|         \______/  \______/ \__| 


 [1] DO YOU NEED ANY GIRL FRIEND 
 [2] HOW MANY GIRL FRIEND DO YOU NEED 
 [3] DO YOU WANT TO EXIT 
'''
# import section start 
from random2 import choice
from time import sleep
import webbrowser as auto
import os
# import section end
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 
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
while True:
    clear_screen()
    print(BANNERR)
    user_input = int(input('WHAT IS YOUR CHOICE : '))
    if user_input==1:
        ok_list =choice(girl_list)
        print(' YOUR GIRLFRIEND ID IS '+ ok_list)
        print(' SHE IS SO CUTE . SHE IS LUCCHA .')
        print('PRESS ENTER ')
        sleep(5)
        auto.open(ok_list)
    elif user_input==2:
        print('YOU ARE FUCK BOY . SO YOU HAVE NO GIRLFRIEND . FUCK YOU')
    elif user_input==3:
        break
    else:
        print('LOGIN ERROR . EARN CRADIT :')
        print('FOLLOW MY ALL ID . AND YT CHANNEL ')
        sleep(5)
        auto.open('https://www.facebook.com/@cybercopbangladesh')
        auto.open('https://www.youtube.com/@cybercopbangladesh')
        auto.open('https://www.github.com/cybercop-404')
# Developer CYBER-COP-BANGLADESH 
