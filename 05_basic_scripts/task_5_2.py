# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111ll111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network_mask = input( "Pls input IP add and mask of netwrok in format X.X.X.X/XX: ")
a = network_mask.split('.') # a0_3 = network ip
b = a[-1].split('/')        # b0 = netwrok ip; b1 = mask


output_template = '''

Network:
{:8} {:8} {:8} {:8}
{:0>8b} {:0>8b} {:0>8b} {:0>8b}

Mask
/{}
{:<8} {:<8} {:<8} {:<8}
{} {} {} {}
'''
mask = (int(b[1])) * '1'
binary_mask = '''{:0<8}{:0<8}{:0<8}{:0<8} '''
out = binary_mask.format(mask[0:8], mask[8:16], mask[16:24], mask[24:32])



print (output_template.format(a[0],a[1],a[2],b[0],
int(a[0]),int(a[1]),int(a[2]),int(b[0]),
b[1],
int(out[0:8],2),int(out[8:16],2),int(out[16:24],2),int(out[24:32],2),
out[0:8],out[8:16],out[16:24],out[24:32]))