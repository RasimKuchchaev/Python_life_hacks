# pip install paramiko - ssh client

import os
import subprocess
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError

IP_ADDRESS = '192.168.102.16'

def ping_host(ip_address):
    output = os.system('ping -c 1 ' + ip_address)
    if output == 0:
        print(f"Хост доступен {output}")
        return True
    else:
        print(f"{output} Хост не доступен")
        return False


    # try:
    #     output = subprocess.check_output(['ping', '-c', '1', ip_address])
    #     return True
    # except subprocess.CalledProcessError:
    #     return False


def search_host_to_network(subnet_start, subnet_stop):
    for i in range(subnet_start, subnet_stop + 1):
        for j in range(1, 255):
            ip_address = "192.168." + str(i) + "." + str(j)
            if ping_host(ip_address):
                print(f"Хост доступен {ip_address}")


def ssh_command_to_host(ip_host, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip_host, port=22, username='root', password='12345678')

        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.write('Входные данные')
        stdin.flush()

        result = stdout.read().decode('utf-8')
        ssh.close()
        print(result)

    except NoValidConnectionsError:
        print(f"Failed to connect {ip_host}")


def main():
    # ping_host(ip_address)
    search_host_to_network(subnet_start=96, subnet_stop=102)
    # ssh_command_to_host(ip_host=IP_ADDRESS, command="sudo dnf install wine -y")


if __name__ == '__main__':
    main()



"""         Фон рабочего стола
gsettings set org.mate.background picture-filename '/home/dgmu/Загрузки/girl-beauty-girl-smile-wallpaper-preview.jpg'
"""


