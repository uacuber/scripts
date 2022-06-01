# -*- coding: utf-8 -*-
"""
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

"""


import textfsm



def parse_command_output(template, command_output):
    with open(template) as f:
        out = []
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        #result = re_table.ParseText(command_output.read())
        result = re_table.ParseText(command_output)
        out.append(header)
        for item in result:
            out.append(item)
        print(out)
        return out


if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/22_textfsm/"
    with open(path + 'output/sh_ip_int_br.txt') as f:
        command_output = f.read()
        parse_command_output(path + 'templates/sh_ip_int_br.template', command_output)