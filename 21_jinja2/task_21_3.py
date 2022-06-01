# -*- coding: utf-8 -*-
"""
Задание 21.3

Создайте шаблон templates/ospf.txt на основе конфигурации OSPF в файле cisco_ospf.txt.
Пример конфигурации дан, чтобы показать синтаксис.

Шаблон надо создавать вручную, скопировав части конфига в соответствующий шаблон.

Какие значения должны быть переменными:
* номер процесса. Имя переменной - process
* router-id. Имя переменной - router_id
* reference-bandwidth. Имя переменной - ref_bw
* интерфейсы, на которых нужно включить OSPF. Имя переменной - ospf_intf
 * на месте этой переменной ожидается список словарей с такими ключами:
  * name - имя интерфейса, вида Fa0/1, Vlan10, Gi0/0
  * ip - IP-адрес интерфейса, вида 10.0.1.1
  * area - номер зоны
  * passive - является ли интерфейс пассивным. Допустимые значения: True или False

Для всех интерфейсов в списке ospf_intf, надо сгенерировать строки:
 network x.x.x.x 0.0.0.0 area x

Если интерфейс пассивный, для него должна быть добавлена строка:
 passive-interface x

Для интерфейсов, которые не являются пассивными, в режиме конфигурации интерфейса,
надо добавить строку:
 ip ospf hello-interval 1


Все команды должны быть в соответствующих режимах.

Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf.yml,
с помощью функции generate_config из задания 21.1.
Не копируйте код функции generate_config.


"""






from jinja2 import Environment, FileSystemLoader
import yaml
from task_21_1 import generate_config

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/21_jinja2/"
    data_file = "data_files/ospf.yml"
    with open(path + data_file) as f:
        info = yaml.safe_load(f)
    print(generate_config('templates/ospf.txt', info))