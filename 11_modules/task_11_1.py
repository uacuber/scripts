# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку,
а затем передать строку как аргумент функции.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
"""
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
"""
            out = {**out, **dic}
    print(out)
    return(out)


Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
"""
def parse_cdp_neighbors(command_output):
    out = {}
    for line in command_output.split("\n"):
        dic = {}

        if 'cdp' in line:
            local_dev = line[0:3]
        elif 'Eth' in line:
            value_in_line = line.split()
            rem_info = (value_in_line[0], value_in_line[-2] + value_in_line[-1] )
            local_info = (local_dev, value_in_line[1] + value_in_line[2])
            dic[local_info] = [rem_info]
            #for a in dic:
            #    out.update(dic)
    print(dic)
    #return(out)
"""

def parse_cdp_neighbors(command_output):
    out = {}
    for line in command_output.split("\n"):
        if 'cdp' in line:
            local_dev = line[0:3]
        elif 'Eth' in line:
            value_in_line = line.split()
            rem_info = (value_in_line[0], value_in_line[-2] + value_in_line[-1])
            local_info = (local_dev, value_in_line[1] + value_in_line[2])
            out[local_info] = rem_info
    #print(out)
    return(out)

with open("/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/11_modules/sh_cdp_n_sw1.txt") as f:
    content = f.read()

parse_cdp_neighbors(content)