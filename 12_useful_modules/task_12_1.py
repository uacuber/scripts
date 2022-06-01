# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



import subprocess

def ping_ip_addresses(input_ip_check):
    can_ping = []
    cant_ping = []
    out = ()
    for ip_add in input_ip_check:
        result = subprocess.run(['ping', '-c', '1', ip_add], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            can_ping.append(ip_add)
        else:
            cant_ping.append(ip_add)
    #print(can_ping)
    #print(cant_ping)
    out = (can_ping, cant_ping)
    #print(out)
    return(out)



input_ip = ['8.8.8.8', '192.168.123.133']

ping_ip_addresses (input_ip)