# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re
import json

regex = (
        r'(\S+) +(\S+ +\S+) +\d+ +\S+ +\S+ +\S+ +\d+ +(\S+ +\S+)'
        )

regex_name = r'(\w+)'

def parse_sh_cdp_neighbors(command_output):
    matches = re.finditer(regex, command_output)
    match_name = re.search(regex_name, command_output)
    device_name = (match_name.group())
    dict_rem = {}
    dict_out = {}
    list_local_int = []
    for match in matches:
        dict_rem[(match.group(1))] = (match.group(3))
        list_local_int.append(match.group(2))
    for value, pair in zip(list_local_int, dict_rem.items()):
        a, b = pair
        dict_out[value] = {a: b}
    out_final = {device_name: dict_out}
    #print(out_final)
    return(out_final)


if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/17_serialization/"
    with open(path + 'sh_cdp_n_sw1.txt') as f:
        content = f.read()
        parse_sh_cdp_neighbors(content)