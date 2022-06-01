# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f = open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/07_files/ospf.txt')
lines = f.readlines()
for line in lines:
    c = line.split() # set from line to value
    c.remove('O')
    f = c[1].strip('[]') # ad found
    g = c[3].strip(',') # nh found
    j = c[4].strip(',') # time
    template = '''
Protocol             OSPF
Prefix:              {}
AD/Metric:           {}
Next-Hop:            {}
Last update:         {}
Outbound Interface:  {}'''


    print (template.format(c[0], f, g, j, c[5]))
#use exampel from 4_6