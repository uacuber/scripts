# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

for line in lines:
    if line[0] != '!':
        a = line.strip()
        if ignore[0] in a or ignore[1] in a or ignore[2] in a:
            pass
        else:
            print(a)


    else:
        for word in ignore:
            if word not in a:
                print(a.strip())

        for word_ig in ignore:
            if not word_ig in line_without_1:
                print(line_without_1)

        for word_ig in ignore:
            if word_ig in output:
                print(output.remove(word_ig))

"""

ignore = ["duplex", "alias", "Current configuration"]


f = open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/07_files/config_sw1.txt')
lines = f.readlines()
ignore_line = False

for line in lines:
    if line[0] != '!':
        line = line.strip()
        for word_ig in ignore:
            if word_ig in line:
                ignore_line = True
                break
            else:
                ignore_line = False
        if ignore_line:
            pass
        else:
            print(line)





