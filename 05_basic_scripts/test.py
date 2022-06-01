# -*- coding: utf-8 -*-

network_mask = input( "Pls input IP add and mask in format x.x.x.x x.x.x.x : ")
a = network_mask.split(' ') # a0=ip a1=mask
b = a[0].split('.') # b0_4= ip add
c = a[1].split('.') # c0_4 = mask

template_ip = '''{:0>8b}{:0>8b}{:0>8b}{:0>8b}'''
# change to binary ip add from input
binary_ip = template_ip.format(int(b[0]), int(b[1]), int(b[2]), int(b[3]))
binary_mask = template_ip.format(int(c[0]), int(c[1]), int(c[2]), int(c[3]))
prefix = binary_mask.count('1')
network_bin_ip = binary_ip[0:prefix]

network_bin_ip_temp = '''{:0<32}'''
broad_bin_ip_temp = '''{:1<32}'''
d = network_bin_ip_temp.format(network_bin_ip) # final bin net
e = broad_bin_ip_temp.format(network_bin_ip) # final bin broad
network_ip1 = (str(int(d[0:8],2)) + '.'+ str(int(d[8:16],2))
+ '.' + str(int(d[16:24],2)) + '.')
network_ip2 = str(int(d[24:32],2))
broad_ip1 = (str(int(e[0:8],2)) + '.'+ str(int(e[8:16],2))
+ '.' + str(int(e[16:24],2)) + '.')
broad_ip2 = str(int(e[24:32],2))
broad_ip = broad_ip1 + broad_ip2
network_ip = network_ip1 + network_ip2
net_ip = (int(d[24:32],2))
router_ip = (int(b[3]))

if router_ip - net_ip == 1:
    peer_ip_last = net_ip + 2
elif router_ip - net_ip == 0:
    peer_ip_last = net_ip
else:
    peer_ip_last = net_ip + 1
peer_ip = network_ip1 + str(peer_ip_last)
first_ip = network_ip1 + str(int(net_ip)+1)
last_ip = (broad_ip1 + str(int(e[24:32],2) - 1))

out_temp = '''
ip_add    {}
mask      {}
network   {}
broad     {}
peer_ip   {}
first_ip  {}
last_ip   {}
'''
print(out_temp.format(a[0], a[1], network_ip, broad_ip, peer_ip, first_ip, last_ip))