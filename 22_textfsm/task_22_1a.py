# -*- coding: utf-8 -*-
"""
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
"""


import textfsm


def parse_output_to_dict(template, command_output):
    with open(template) as f:
        out_list = []
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        #result = re_table.ParseText(command_output.read())
        result = re_table.ParseText(command_output)
        for item in result:
            out_dic = {}
            for key, value in zip(header, item):
                out_dic[key] = value
            out_list.append(out_dic)
        print(out_list)
        return out_list

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/22_textfsm/"
    with open(path + 'output/sh_ip_int_br.txt') as f:
        command_output = f.read()
        parse_output_to_dict(path + 'templates/sh_ip_int_br.template', command_output)