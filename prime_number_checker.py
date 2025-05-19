import re
from colorama import init, Fore, Back, Style

# initialize colorama
init(autoreset=True)

while True:
    num = input('please input the number you want to check whether it\' prime, input \'exit()\' to quit')
        
    if num == 'exit()':# check whether it's a quit command
        print(Fore.GREEN+"Script quit")
        break
    try:
        number = int(num) 
        bool = not re.match(r'^.?$|^(..+?)\1+$', '1'*number)# the magic regular expression
        if bool == True:
            print(Fore.BLUE+'{} is a prime number'.format(num))
        else: print(Fore.BLUE+'{} is not a prime number'.format(num))
    
    except ValueError:
            print(Fore.RED+"{} is not a number, please input correctly".format(num))
