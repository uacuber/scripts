# -*- coding: utf-8 -*-
"""
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""
import clitable
import textfsm

def parse_command_dynamic(command_output, attributes_dict, index_file='index', templ_path='templates'):
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    data_rows = [list(row) for row in cli_table]
    out_list = []
    for row in data_rows:
        out_dic = {}
        for key, value in zip(cli_table.header, row):
            out_dic[key] = value
        out_list.append(out_dic)
    print(out_list)
    return out_list

if __name__ == "__main__":
    attributes_dict = {
        'Command': 'sh ip int br',
        'Vendor': "cisco_ios",
            }
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/22_textfsm/"
    with open(path + 'output/sh_ip_int_br.txt') as f:
        command_output = f.read()
        parse_command_dynamic(command_output, attributes_dict)