# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re

regex2 = (
        r'interface (\S+)\n'
        r' description \S+ \S+ \S+'
        )

regex1 = (
        r'\n'
        r'interface (\S+)\n'
        )

def get_ints_without_description(file_name):
    with open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/15_module_re/' + file_name) as f:
        matches1 = re.findall(regex1, f.read())
        #print(matches1)
    with open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/15_module_re/' + file_name) as f:
        matches2 = re.findall(regex2, f.read())
        #print(matches2)
    out = [x for x in matches1 if x not in matches2]
    print(out)
    return(out)


get_ints_without_description('config_r1.txt')