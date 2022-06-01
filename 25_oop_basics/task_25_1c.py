# -*- coding: utf-8 -*-

"""
Задание 25.1c

Изменить класс Topology из задания 25.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

"""

class Topology:
    def __init__(self, data):
        self.data = data
        out_dic = {}
        for key, value in self.data.items():
           key, value = sorted([key, value])
           out_dic[key] = value
        topology = (out_dic)
        self.topology = topology

    def delete_link(self, del_value1, del_value2):
        if (del_value1, del_value2) not in self.topology.items() and (del_value2, del_value1) not in self.topology.items():
            print('Такого соединения нет')
        self.topology = {key:value for key, value in self.topology.items() if key != del_value1}
        self.topology = {key:value for key, value in self.topology.items() if key != del_value2}
        print(self.topology)

    def delete_node(self, node):
        del_dic = {}
        for key, value in self.topology.items():

            if node not in key and node not in value:
                del_dic[key] = value
            else:
                print('Такого устройства нет')
        #print(del_dic)
'''
topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

top = Topology(topology_example)
top.topology
top.delete_node('R1')