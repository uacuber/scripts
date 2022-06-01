# -*- coding: utf-8 -*-
"""
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""


from netmiko import ConnectHandler
import yaml
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
        return output
    except NetMikoAuthenticationException as error1:
        print(error1)
    except NetMikoTimeoutException as error2:
        print(error2)


if __name__ == "__main__":
    command = "sh ip int br"
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/19_ssh_telnet/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        print(send_show_command(device, command))