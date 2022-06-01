# -*- coding: utf-8 -*-

"""
Задание 25.2b

Скопировать класс CiscoTelnet из задания 25.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного режима или список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_25_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

"""
import telnetlib
import time
import clitable
import textfsm

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

    def send_config_commands(self, commands, enable_password=True):
        self.telnet.write(b"conf t\n")
        time.sleep(1)
        if type(commands) == str:
            self.telnet.write(commands.encode("ascii") + b"\n")
            time.sleep(1)
            output = self.telnet.read_very_eager().decode("ascii")
            return output
        else:
            for command in commands:
                self.telnet.write(command.encode("ascii") + b"\n")
                time.sleep(1)
            output = self.telnet.read_very_eager().decode("ascii")
            return output



r1_params = {
            'ip': '192.168.100.1',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'}

r1 = CiscoTelnet(**r1_params)
#print(r1.send_show_command('sh ip int br', parse=True))
print(r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255']))