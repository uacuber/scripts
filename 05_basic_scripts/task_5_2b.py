# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv # только две строки поменял

network_mask = argv[1] # только две строки поменял
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