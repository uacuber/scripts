# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
while True:
    try:
        a = int(input('aqdasda'))
    except (ValueError, IndexError):
        print('Неправильный IP-адрес')
        continue
    else:
        break

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    try:
        ip_add = input('pls input ip add x.x.x.x: ')
        ip_split = str(ip_add).split('.')
        ip_check = int(ip_split[0])
        #хотел зделать цикл, чтоб каждое число из октета брати в ицкле а не вручную
        #не нашол как сделать
        if int(ip_split[0]) < 255 and int(ip_split[1]) < 255 and int(ip_split[2]) < 255 and int(ip_split[3]) < 255:
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
        else:
            print('Неправильный IP-адрес')
            continue
    except (ValueError, IndexError):
        print('Неправильный IP-адрес')
        continue
    else:
        break