# -*- coding: utf-8 -*-
"""
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""

from netmiko import ConnectHandler
import yaml
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import logging



def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        prompt = ssh.find_prompt()
        output = ssh.send_command(command)
    return (prompt + command + '\n' +output)




def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(limit) as executor:
        result = executor.map(send_show_command, devices, repeat(command))
    for info in result:
        #path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/20_concurrent_connections/"
        f_out = open(filename, 'a') # path + filename писал но ругался тест
        f_out.write(info)
        print(info)


if __name__ == "__main__":
    command = "sh ip int br"
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/20_concurrent_connections/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_show_command_to_devices(devices, command, '1.txt')

'''
from netmiko import ConnectHandler
import yaml

def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
    return output

if __name__ == "__main__":
    command = "sh ip int br"
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/20_concurrent_connections/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        print(send_show_command(device, command))
'''