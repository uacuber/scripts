# -*- coding: utf-8 -*-
"""
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""



from netmiko import ConnectHandler
import yaml
import sys

def send_config_commands(device, config_commands, log=True):
    with ConnectHandler(**device) as ssh:
        if log:
            print('Подключаюсь к ' + device['ip'] + '...')
        ssh.enable()
        dict_good = {}
        dict_bad = {}
        out = ()
        for command in config_commands:
            output = ssh.send_config_set(command)
            if 'Incomplete command' in output:
                print('Команда "' + command + '" выполнилась с ошибкой "' + ((output.split('\n'))[3]).lstrip('% ') + '" на устройстве ' + device['ip'])
                dict_bad[command] = output
                answer = input('Продолжать выполнять команды? [y]/n: ')
                if answer == 'n' or answer == 'no':
                    break
            elif 'Invalid input' in output:
                print('Команда "' + command + '" выполнилась с ошибкой "' + ((output.split('\n'))[4]).lstrip('% ') + '" на устройстве ' + device['ip'])
                dict_bad[command] = output
                answer = input('Продолжать выполнять команды? [y]/n: ')
                if answer == 'n' or answer == 'no':
                    break
            elif 'Ambiguous' in output:
                print('Команда "' + command + '" выполнилась с ошибкой "' + ((output.split('\n'))[3]).lstrip('% ') + '" на устройстве ' + device['ip'])
                dict_bad[command] = output
                answer = input('Продолжать выполнять команды? [y]/n: ')
                if answer == 'n' or answer == 'no':
                    break
            else:
                dict_good[command] = output
        out = (dict_good, dict_bad)
        return(out)


if __name__ == "__main__":
    commands_with_errors = ["logging 0255.255.1", "logging", "a"]
    correct_commands = ["logging buffered 20010", "ip http server"]
    commands = commands_with_errors + correct_commands
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/19_ssh_telnet/"
    with open(path + "devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        (send_config_commands(device, commands))