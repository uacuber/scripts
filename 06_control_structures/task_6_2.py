# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_add = input('pls input ip add x.x.x.x: ')
ip_split = str(ip_add).split('.')
ip_check = int(ip_split[0])
if ip_add == '0.0.0.0':
    print ('unassigned')
elif ip_add == '255.255.255.255':
    print ('local broadcast')
elif ip_check > 224:
    print ('multicast')
elif ip_check > 1:
    print ('unicast')
else:
    print('unused')



