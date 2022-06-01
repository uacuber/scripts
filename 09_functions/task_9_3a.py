# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
            if 'interface F' in line:
                int_ac = (line.split()[1])
            elif 'access v' in line:
                access = int(line.split()[3])
                dic_ac[int_ac] = access
            elif 'switchport mode access\n duplex auto' in line:
                print(1)
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
    print(tup_out)
    return(tup_out)

'''

"""


def get_int_vlan_map(config_filename):
    dic_ac = {}
    dic_tr = {}
    tup_out = ()
    with open(config_filename) as file:
        for line in file:
            if 'interface F' in line:
                int_ac = (line.split()[1])
                if 'mode access' in line:
                    if 'access v' in line:
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
    print(tup_out)
    #return(tup_out)



get_int_vlan_map('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/09_functions/config_sw2.txt')


