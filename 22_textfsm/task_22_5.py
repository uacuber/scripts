# -*- coding: utf-8 -*-
"""
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию
send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
"""
import yaml
from itertools import repeat
from task_22_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor


def send_and_parse_command_parallel(devices, command):
    with ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(send_and_parse_show_command, devices, repeat(command), repeat('templates'))
        return result

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/22_textfsm/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
        send_and_parse_command_parallel(devices, 'sh ip int br')