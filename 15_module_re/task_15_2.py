# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""

import re

regex = (#r'Interface .*\n'
        r'(\S+) +(\S+) +(\S+) +(\S+) +(\w+ \w+|\w+) +(up|down)' # logical can be up or down
        )

def parse_sh_ip_int_br(filename):
    out = []
    with open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/15_module_re/' + filename) as f:
        matches = re.finditer(regex, f.read())
        for match in matches:
            out.append(match.group(1, 2, 5, 6))
        print(out)
        return(out)


parse_sh_ip_int_br('sh_ip_int_br.txt')