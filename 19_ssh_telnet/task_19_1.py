# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

"""

from netmiko import ConnectHandler
import yaml



def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
    return output



if __name__ == "__main__":
    command = "sh ip int br"
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/19_ssh_telnet/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        print(send_show_command(device, command))