# -*- coding: utf-8 -*-
"""
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import sys
with open(sys.argv[1], 'r') as my_file:  #googled steps, don`t found in book
    f = open(sys.argv[1])

#f = open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/07_files/config_sw1.txt')
    lines = f.readlines()
    for line in lines:
        if line[0] != '!':
            print(line.strip())