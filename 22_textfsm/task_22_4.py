# -*- coding: utf-8 -*-
"""
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным
Template, Hostname, Vendor, Command
sh_cdp_n_det.template, .*, cisco_ios, sh[[ow]] cdp ne[[ighbors]] de[[tail]]
{'device_type': 'cisco_ios', 'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}

 'Command': 'sh ip int br',
        'Vendor': "cisco_ios",

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
"""
import yaml
from netmiko import ConnectHandler
import clitable
import textfsm

def send_and_parse_show_command(device_dict, command, templates_path, index='index'):
    with ConnectHandler(**device_dict) as dev:
        dev.enable()
        command_out = dev.send_command(command)
    cli_table = clitable.CliTable(index, templates_path)
    attributes_dict = {
        'Command': command,
        'Vendor': "cisco_ios",
                        }
    # не понял нужно ли создавать attributes_dict, но не понял как сделать из device_dict->attributes_dict
    # ну можна додать ключ-значения до существующего словаря, но не вижу смисла
    cli_table.ParseCmd(command_out, attributes_dict)
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
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/22_textfsm/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_and_parse_show_command(devices[0], 'sh ip int br', 'templates')