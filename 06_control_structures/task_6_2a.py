# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

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
except (ValueError, IndexError):
    print('Неправильный IP-адрес')