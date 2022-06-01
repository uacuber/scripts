# -*- coding: utf-8 -*-

"""
Задание 25.2c

Скопировать класс CiscoTelnet из задания 25.2b и изменить метод send_config_commands добавив проверку команд на ошибки.

У метода send_config_commands должен быть дополнительный параметр strict:
* strict=True значит, что при обнаружении ошибки, необходимо сгенерировать исключение ValueError
* strict=False значит, что при обнаружении ошибки, надо только вывести на стандартный поток вывода сообщене об ошибке

Метод дожен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).
Текст исключения и ошибки в примере ниже.

Пример создания экземпляра класса:
In [1]: from task_25_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Использование метода send_config_commands:

In [7]: print(r1.send_config_commands(commands, strict=False))
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
При выполнении команды "i" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "i"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.

"""

import telnetlib
import time
import clitable
import textfsm
import re

class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self.telnet.write(username.encode("ascii") + b"\n")
        self.telnet.read_until(b"Password:")
        self.telnet.write(password.encode("ascii") + b"\n")
        self.telnet.write(b"enable\n")
        self.telnet.read_until(b"Password:")
        self.telnet.write(secret.encode("ascii") + b"\n")
        time.sleep(1)
        self.telnet.read_very_eager()

    def send_show_command(self, command, parse, templates = 'templates'):
        self.telnet.write(command.encode("ascii") + b"\n")
        time.sleep(1)
        output = self.telnet.read_very_eager().decode("ascii")
        if parse == False:
            print(output)
        else:
            cli_table = clitable.CliTable('index', templates)
            attributes_dict = {
                'Command': command,
                'Vendor': "cisco_ios",
                            }
            cli_table.ParseCmd(output, attributes_dict)
            data_rows = [list(row) for row in cli_table]
            out_list = []
            for row in data_rows:
                out_dic = {}
                for key, value in zip(cli_table.header, row):
                    out_dic[key] = value
                out_list.append(out_dic)
            print(out_list)
            return out_list

    def _write_line(self, command, enable_password=True):
        self.telnet.write(b"conf t\n")
        time.sleep(1)
        self.telnet.write(command.encode("ascii") + b"\n")
        time.sleep(1)
        output = self.telnet.read_very_eager().decode("ascii")
        return output

    def send_config_commands(self, commands, strict=True, enable_password=True):
        self.telnet.write(b"conf t\n")
        time.sleep(1)
        if type(commands) == str:
            self.telnet.write(commands.encode("ascii") + b"\n")
            time.sleep(1)
            output = self.telnet.read_very_eager().decode("ascii")
            self.check_errors(output, commands, strict)
            return output
        else:
            for command in commands:
                self.telnet.write(command.encode("ascii") + b"\n")
                time.sleep(1)
            output = self.telnet.read_very_eager().decode("ascii")
            self.check_errors(output, command, strict)
            return output

    def check_errors(self, output, command, strict):
        regex = "% (?P<errmsg>.+)"
        error_in_result = re.search(regex, output)
        if error_in_result:
            er_name = error_in_result.group("errmsg")
            if strict:
                if "Invalid input detected" in output:
                    raise ValueError('При выполнении команды "'
                                    + command + '" на устройстве ' + r1_params['ip']
                                    + ' возникла ошибка ' + er_name)
            else:
                error_message = 'При выполнении команды "{}" на устройстве {} возникла ошибка {}'
                print(error_message.format(command, r1_params['ip'], er_name))
            print(output)


r1_params = {
            'ip': '192.168.100.1',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'}
commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']
commands = commands_with_errors+correct_commands
correct_commands = ["interface loop55", "ip address 5.5.5.5 255.255.255.255"]
r1 = CiscoTelnet(**r1_params)
print(r1.send_config_commands(correct_commands, strict=False))
#print(r1.send_show_command('sh ip int br', parse=True))
#print(r1.send_config_commands(['logging 0255.255.1'], strict=True))