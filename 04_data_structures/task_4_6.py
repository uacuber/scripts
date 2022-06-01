# -*- coding: utf-8 -*-
"""
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

a = ospf_route.split() # set from line to value
c = list(a) # convert to list, I can found each value 0,1...7
c.remove('O')
f = str(c[1]).strip('[]') # ad found
g = str(c[3]).strip(',') # nh found
j = str(c[4]).strip(',') # time
template = '''
Protocol             OSPF
Prefix:              {}
AD/Metric:           {}
Next-Hop:            {}
Last update:         {}
Outbound Interface:  {}'''

#print (c)
print (template.format(c[0], f, g, j, c[5]))