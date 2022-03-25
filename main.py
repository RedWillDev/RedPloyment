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
printssh1="SSH - Configuration"
printssh2="SSH - Fail2Ban"
port_random=set_ssh_port()

#VAR Fail2Ban
path_to_jail_local="/etc/fail2ban/jail.local"

#VAR GENERALE
done='true'

#CONFIGURE SSH


def ssh_conf():
    global done
    print(printssh1)
    #animate()
    try:
        #os.system("sed -i 's/#   Port 22/    Port {}/'".format(port_random) + "{}".format(path_to_ssh_conf))
        os.system("sudo sed -i 's/#Port 22/Port {}/' {}".format(port_random, path_to_sshd_conf))
        os.system("sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' {}".format(path_to_sshd_conf))
    except:
        print("an error as occured verify you file path")
    finally:
        os.system("sudo systemctl restart sshd ssh")
        #done="true"
        print(Fore.RED + "SSH" + Fore.RESET + " port set to : " + Fore.RED + str(port_random) + "\n" +
              "Root" + Fore.RESET + " remote login : " + Fore.RED + "disabled" + "\n" +
               "SSH, SSHD correctly restarted" + Fore.RESET)
        #done="false"

def Fail2Ban():
    global done
#    animate()
    try:
        os.system("sudo apt-get install fail2ban -y")
        os.system("sudo cp /etc/fail2ban/jail.{conf,local}")
        os.system("sudo sed -i 's/bantime  = 10m/bantime  = -1/ {}'".format(path_to_jail_local))
        os.system("sudo sed -i 's/findtime  = 10m/findtime  = 15m/ {}'".format(path_to_jail_local))
        os.system("sudo sed -i 's/maxretry = 5/maxretry = 3/ {}'".format(path_to_jail_local))
        os.system("sudo sed -i 's/maxretry = 5/maxretry = 3/ {}'".format(path_to_jail_local))
    except:
        print("an error as occured verify you file path")

    finally:
        os.system("sudo systemctl enable fail2ban && sudo systemctl restart fail2ban")
        #done="true"
        print(Fore.RED + "Bantime" + Fore.RESET + " set to : " + Fore.RED + "-1" + "\n" +
              "Findtime" + Fore.RESET + " set to : " + Fore.RED + "15m" + "\n" +
              "Maxretry" + Fore.RESET + " set to : " + Fore.RED + "3" + "\n" +
              "Fail2Ban correctly restarted")
       # done="false"




ssh_conf()
time.sleep(3)
Fail2Ban()