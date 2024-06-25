# pip install paramiko - ssh client

import os
import subprocess

import asyncio
import aioping
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, SSHException

IP_ADDRESS = '192.168.102.16'
IP_LIST = []

LOGIN_SSH = 'root'
PASSWORD_SSH = '12345678'

async def ping_host_asyncio(ip):
    try:
        delay = await aioping.ping(ip)
        print(f"{ip}: Ping successful, delay = {delay} ms")
        IP_LIST.append(ip)
    except TimeoutError:
        print(f"{ip}: Ping timeout")

async def search_host_to_network_asyncio(subnet_start, subnet_stop):
    task = [ping_host_asyncio("192.168." + str(i) + "." + str(j)) for i in range(subnet_start, subnet_stop + 1)
            for j in range(1, 255)]
    await asyncio.gather(*task)

# if __name__ == '__main__':
#     asyncio.run(search_host_to_network_asyncio(96, 102))

# def ping_host(ip_address):
#     output = os.system('ping -c 1 ' + ip_address)
#     if output == 0:
#         print(f"Хост доступен {output}")
#         return True
#     else:
#         print(f"{output} Хост не доступен")
#         return False


    # try:
    #     output = subprocess.check_output(['ping', '-c', '1', ip_address])
    #     return True
    # except subprocess.CalledProcessError:
    #     return False


# def search_host_to_network(subnet_start, subnet_stop):
#     for i in range(subnet_start, subnet_stop + 1):
#         for j in range(1, 255):
#             ip_address = "192.168." + str(i) + "." + str(j)
#             if ping_host(ip_address):
#                 print(f"Хост доступен {ip_address}")


def ssh_command_to_host(ip_host, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip_host, port=22, username= LOGIN_SSH, password=PASSWORD_SSH)

        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.write('Входные данные')
        stdin.flush()

        result = stdout.read().decode('utf-8')
        ssh.close()
        print(f"--------INFO--------IP-{ip_host}-------{command}--------")
        # print(result)

    except NoValidConnectionsError:
        print(f"Failed to connect {ip_host}")
    except SSHException:
        print(f"No existing session {ip_host}")
    except TimeoutError:
        print(f"TimeoutError123 {ip_host}")


def main():
    asyncio.run(search_host_to_network_asyncio(96, 102))
    # ping_host(ip_address)
    # search_host_to_network(subnet_start=96, subnet_stop=102)
    for ip_addr in IP_LIST:
        ssh_command_to_host(ip_host=ip_addr, command="sudo dnf install wine -y")


if __name__ == '__main__':
    main()




"""         Фон рабочего стола
gsettings set org.mate.background picture-filename '/home/dgmu/Загрузки/girl-beauty-girl-smile-wallpaper-preview.jpg'
"""

# scp -r /mnt/a1056def-4df1-4959-9904-5b654aed0dfd/Soft/Rasim/medacad/medic/ root@192.168.102.16:'/home/dgmu/Рабочий\ стол/medic/'


