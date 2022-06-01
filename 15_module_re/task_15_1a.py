# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""


import re

regex = (r'interface (?P<interf>\S+)'
        #r'(.*\n)+?\n'
        r'ip .*'
        )

def get_ip_from_cfg(file_name):
    out = {}
    with open('/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/15_module_re/' + file_name) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == 'interf':
                    interf = match.group(match.lastgroup)
                    out[interf] = {}
        print(out)


get_ip_from_cfg('config_r1.txt')