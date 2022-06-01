# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']


'''
        if ipaddress.ip_address(value):
            print(value)
        elif int ((value.split('-'))[1]) in range(0, 255):
            print(value)
        else:
            print(1)

'''

"""
import ipaddress

def convert_ranges_to_ip_list(input_ip):
    out_list = []
    for value in input_ip:
        if (len(value.split('.'))) == 4:
            if len(value.split('-')) == 2:
                ip_add_first = ((value.split('-')[0]))
                out_list.append(ip_add_first)
                octet = (value.split('-')[1])
                for i in range(int(ip_add_first.split('.')[3]) , int(octet)):
                    out_list.append(str(ipaddress.ip_address(ip_add_first) + (i + 1 - int(ip_add_first.split('.')[3]))))
            else:
                out_list.append(value)
        else:
            ip_add_first_r = ((value.split('-')[0]))
            out_list.append(ip_add_first_r)
            ip_add_last_r = ((value.split('-')[1]))
            for x in range(int(ip_add_first_r.split('.')[3]), int(ip_add_last_r.split('.')[3])):
                out_list.append(str(ipaddress.ip_address(ip_add_first_r) + (x + 1 -int(ip_add_first_r.split('.')[3]))))
    #print(out_list)
    return(out_list)




ip_test = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
convert_ranges_to_ip_list(ip_test)