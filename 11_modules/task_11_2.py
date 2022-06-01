# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов,
в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать
схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
import graphviz
from draw_network_graph import draw_topology



def create_network_map(filenames):
    out = {}
    out_uniq = {}
    for files in filenames:
        #print(files)
        f = open("/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/11_modules/" + files)
        for line in f:
            line.split("\n")
            #print(line.split("\n"))
            if 'cdp' in line:
                local_dev = (line.split('>'))[0]
                #print(local_dev)
            elif 'Eth' in line:
                value_in_line = line.split()
                rem_info = (value_in_line[0], value_in_line[-2] + value_in_line[-1])
                local_info = (local_dev, value_in_line[1] + value_in_line[2])
                out[local_info] = rem_info
    #print(out)
    uniq_out = {}
    for (key, value) in out.items():
        if key not in uniq_out.values() and key not in uniq_out.keys() and value not in uniq_out.keys() and value not in uniq_out.values():
            uniq_out[key] = value
        #elif value not in uniq_out.keys():
        #    uniq_out[key] = [value]
    #print(uniq_out)
    return(uniq_out)
    draw_topology(uniq_out, '/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/11_modules/1.svg')

# create_network_map(['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt'])
infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]
topology = create_network_map(infiles)
draw_topology(topology)