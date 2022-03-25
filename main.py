import random
import os
import time
import sys
from colorama import init, Fore, Back, Style



#Functiun
def animate():
    while done == 'false':
        sys.stdout.write('\r*-___ |')
        time.sleep(0.3)
        sys.stdout.write('\r/_-__ /')
        time.sleep(0.3)
        sys.stdout.write('\r*__-_ |')
        time.sleep(0.3)
        sys.stdout.write('\r*___- \\')
        time.sleep(0.3)
    sys.stdout.write('\rSucceed     ')



def set_ssh_port():
    rand = random.randint(22000, 59000)
    return rand


#VAR_SSH
path_to_ssh_conf = "/etc/ssh/ssh_config"
path_to_sshd_conf = "/etc/ssh/sshd_config"
printssh1="SSH Configuration"
port_random=set_ssh_port()


#VAR GENERALE
done='false'

#CONFIGURE SSH

def ssh_conf():
    print(printssh1)
    animate()
    try:
        #os.system("sed -i 's/#   Port 22/    Port {}/'".format(port_random) + "{}".format(path_to_ssh_conf))
        os.system("sed -i 's/#Port 22/Port {}/'".format(port_random) + "{}".format(path_to_sshd_conf))
        os.system("sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/'".format(port_random) + "{}".format(path_to_sshd_conf))

    except:
        print("an error as occured verify you file path")
    finally:
        done="true"
        print(Fore.RED + "SSH" + Fore.RESET + " port set to : " + Fore.RED + str(port_random) + "\n" +
              "Root" + Fore.RESET + " remote login : " + Fore.RED + "disabled" + "\n"
                                                                                 "")

