# pip install paramiko - ssh client

import subprocess
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError


def ping_host(ip_address):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip_address])
        return True
    except subprocess.CalledProcessError:
        return False

# ip_address = '192.168.101.232'
# if ping_host(ip_address):
#     print(f"Хост доступен {ip_address}")
# else:
#     print(f"Хост не доступен {ip_address}")

# for i in range(101, 102):
#     # print(i)
#     for j in range(1, 255):
#         ip_address = "192.168." + str(i) + "." + str(j)
#         # print(f"192.168.{i}.{j}")
#         print(ip_address)
#         if ping_host(ip_address):
#             print(f"Хост доступен {ip_address}")


def ssh_command_to_host(ip_host, command, title=None):
    if title!=None:
        print(title)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.write('Входные данные')
    stdin.flush()

    result = stdout.read().decode('utf-8')
    return result

ip_address = '192.168.102.16'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip_address, port=22, username='root', password='12345678')
except NoValidConnectionsError:
    print(1111)
    exit(0)


ssh_wine = ssh_command_to_host(ip_host=ip_address, command="wine --version")
if ssh_wine.startswith('wine'):
    print(ssh_wine)
else:
    ssh_command_to_host(ip_host=ip_address, command='sudo dnf install wine -y', title="install wine")


ssh.close()

"""         Фон рабочего стола
gsettings set org.mate.background picture-filename '/home/dgmu/Загрузки/girl-beauty-girl-smile-wallpaper-preview.jpg'
"""


