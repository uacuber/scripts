# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
'''
def get_int_vlan_map(config_filename):
    filt_data = []
    tup = ()
    dic = {}
    with open(config_filename) as file:
        for line in file:
            line.strip()
            if 'interface F' in line or 'access v' in line or 'trunk all' in line:
                a = (line.strip())
                filt_data.append(a)
        #print(filt_data)
        for data_int in filt_data:
           if  'interface F' in data_int:
               if (len(filt_data)-1) != filt_data.index(data_int):
                    #print(filt_data.index(data_int))

                    aa = (filt_data[(filt_data.index(data_int))+1])
                    dic[data_int] = aa
        print(dic)
        for key in dic:
            print(key)
'''


'''
        access_dict = {}
        for access in filt_data:
            if 'access v' in access:
                print(access)
                index_acc = filt_data.index(access)
                #print(filt_data.index(access))
                #print(filt_data[index_acc-1])
                port_acc = (filt_data[index_acc-1]).strip('interface ')
                access_dict[port_acc] = access.strip('switchport access vlan ')
        #print(access_dict)
        #tup = access_dict, access_dict
        #return(tup)

                    if 'access v' in line:
                print(line.split()[3])




        for line in file:
            if 'interface F' in line:
                int_ac = (line.split()[1])
            elif 'access v' in line:
                access = (line.split()[3])
                dic_ac[int_ac] = access
        print(dic_ac)
'''

def get_int_vlan_map(config_filename):
    dic_ac = {}
    dic_tr = {}
    tup_out = ()
    with open(config_filename) as file:
        for line in file:
            if 'interface F' in line:
                int_ac = (line.split()[1])
            elif 'access v' in line:
                access = int(line.split()[3])
                dic_ac[int_ac] = access
        #print(dic_ac)
    # решил еще раз открить файл и написать новий словарь. не понял как не откривая ето сделать
    with open(config_filename) as file1:
        for line1 in file1:
            trunk_out = []
            if 'interface F' in line1:
                int_tr = (line1.split()[1])
            elif 'trunk all' in line1:
                trunk = (line1.split()[4]).split(',')
                for trunk_vlan in trunk:
                    trunk_out.append(int(trunk_vlan))
                dic_tr[int_tr] = trunk_out
        #print(dic_tr)
    tup_out = dic_ac, dic_tr
    #print(tup_out)
    return(tup_out)




get_int_vlan_map('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/09_functions/config_sw1.txt')