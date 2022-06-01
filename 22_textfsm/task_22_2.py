# -*- coding: utf-8 -*-
"""
Задание 22.2

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding
и записать его в файл templates/sh_ip_dhcp_snooping.template

Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 22.1.

MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69   10.1.5.2         63951       dhcp-snooping   5     FastEthernet0/10
00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
00:09:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/3
Total number of bindings: 4



Value Network (([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}))
Value Mask (\/\d{1,2})
Value Distance (\d+)
Value Metric (\d+)
Value List NextHop ([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})

Start
  ^O -> Continue.Record
  ^O +${Network}${Mask}\s\[${Distance}\/${Metric}\]\svia\s${NextHop},
  ^\s+\[${Distance}\/${Metric}\]\svia\s${NextHop},




Value intf (\S+)
Value address (\S+)
Value status (up|down|administratively down)
Value protocol (up|down)

Start
  ^${intf}\s+${address}\s+\w+\s+\w+\s+${status}\s+${protocol} -> Record


"""

from task_22_1 import parse_command_output

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/22_textfsm/"
    with open(path + 'output/sh_ip_dhcp_snooping.txt') as f:
        command_output = f.read()
        parse_command_output(path + 'templates/sh_ip_dhcp_snooping.template', command_output)