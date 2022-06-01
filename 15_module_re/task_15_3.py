# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re

regex = (
        r'.* static +(\w+) +(\S+) +(\d+) +(.*) +(\d+)'
        )

translate_template = '''object network LOCAL_{}
 host {}
 nat (inside,outside) static interface service {} {} {}'''

def convert_ios_nat_to_asa(need_conv_f, out_f):
    with open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/15_module_re/' + need_conv_f) as f:
        matches = re.finditer(regex, f.read())
        for match in matches:
            #print(match.groups())
            out = (translate_template.format(match.group(2), match.group(2), match.group(1), match.group(3), match.group(5)))
            f2 = open(out_f, 'a')
            f2.write(out + '\n')
            f2.close()
            #print(out)
            #print(match.group(1))

convert_ios_nat_to_asa('cisco_nat_config.txt', '1.txt')