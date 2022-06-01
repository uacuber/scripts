# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает
вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21


Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.

"""

'''
def write_dhcp_snooping_to_csv(filenames, output):
    for file in filenames:
        with open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/17_serialization/' +
        file) as f, open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/17_serialization/' +
        output, 'a') as result:
            out = ['switch', 'mac', 'ip', 'vlan', 'interface']
            wr = csv.writer(result)
            wr.writerow(out)
            name = str(file[0:3])
            for line in f:
                matches = re.search(regex, line)
                if matches:
                    found = (list(matches.groups()))
                    found.insert(0, name)
                    wr.writerow(found)

list_input = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
write_dhcp_snooping_to_csv(list_input, 'result.csv')
'''


import re
import csv
regex = r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)'
def write_dhcp_snooping_to_csv(filenames, output):
    for file in filenames:
        if file == 'sw1_dhcp_snooping.txt':
            with open(file) as f, open(output, 'w') as result:
                out = ['switch', 'mac', 'ip', 'vlan', 'interface']
                wr = csv.writer(result)
                wr.writerow(out)
                name = str(file[0:3])
                for line in f:
                    matches = re.search(regex, line)
                    if matches:
                        found = (list(matches.groups()))
                        found.insert(0, name)
                        wr.writerow(found)
        else:
            with open(file) as f, open(output, 'a') as result:
                wr = csv.writer(result)
                name = str(file[0:3])
                for line in f:
                    matches = re.search(regex, line)
                    if matches:
                        found = (list(matches.groups()))
                        found.insert(0, name)
                        wr.writerow(found)
if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/17_serialization/"
    list_input = [path + 'sw1_dhcp_snooping.txt',
                  path + 'sw2_dhcp_snooping.txt',
                  path + 'sw3_dhcp_snooping.txt']
    write_dhcp_snooping_to_csv(list_input, path + 'output.csv')