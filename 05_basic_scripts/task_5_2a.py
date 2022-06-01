# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

network_mask = input( "Pls input IP add and mask in format X.X.X.X/XX: ")
a = network_mask.split('.') # a0_3 = network ip
b = a[-1].split('/')        # b0 = netwrok ip; b1 = mask

template_ip = '''{:0>8b}{:0>8b}{:0>8b}{:0>8b}'''
# change to binary ip add from input
binary_ip = template_ip.format(int(a[0]), int(a[1]), int(a[2]), int(b[0]))

print (network_mask) # удобно смотреть, что ти ввел - по заданию не нада
output_template = '''
Network:
{:<8} {:<8} {:<8} {:<8}
{} {} {} {}

Mask
/{}
{:<8} {:<8} {:<8} {:<8}
{} {} {} {}
'''
mask = int(b[1]) # int from input prefix
mask_b = (int(b[1])) * '1' # translate prefix to binary
binary_mask = '''{:0<8}{:0<8}{:0<8}{:0<8} '''
# mask go to 1 - another go to 0
out = binary_mask.format(mask_b[0:8], mask_b[8:16], mask_b[16:24], mask_b[24:32])
# found network bin = get ip add to mask lenght
network_ip = binary_ip[0:mask]
ip_bin = '''{:0<32}'''
# found network bin add = just put 0 to the end
final_ip = ip_bin.format(network_ip)  # ip add in bin
# first make print like otput_template
# then add /n for better view

print (output_template.format(int(final_ip[0:8],2), int(final_ip[8:16],2),
int(final_ip[16:24],2), int(final_ip[24:32],2),
final_ip[0:8], final_ip[8:16], final_ip[16:24], final_ip[24:32],
b[1],
int(out[0:8],2),int(out[8:16],2),int(out[16:24],2),int(out[24:32],2),
out[0:8],out[8:16],out[16:24],out[24:32]))