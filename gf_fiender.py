BANNERR = '''\033[0;32m
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
 [2] HOW MANY GIRL FRIEND DO YOU NEED 
 [3] DO YOU WANT TO EXIT 
'''
# import section start 
from random2 import choice
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
        print(' YOUR GIRLFRIEND ID IS '+    ok_list)
        print(' SHE IS SO CUTE . SHE IS LUCCHA .')
        print(ok_list)
        sleep(20)
        break
    elif user_input==2:
        print('YOU ARE FUCK BOY . SO YOU HAVE NO GIRLFRIEND . FUCK YOU')
        sleep(20)
        break
    elif user_input==3:
        break
    else:
        print('LOGIN ERROR . EARN CRADIT :')
        break
# phone verson ditected . 
# Developer CYBER-COP-BANGLADESH 
