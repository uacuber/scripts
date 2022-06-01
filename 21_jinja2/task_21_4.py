# -*- coding: utf-8 -*-
"""
Задание 21.4

Создайте шаблон templates/add_vlan_to_switch.txt, который будет использоваться
при необходимости добавить VLAN на коммутатор.

В шаблоне должны поддерживаться возможности:
* добавления VLAN и имени VLAN
* добавления VLAN как access, на указанном интерфейсе
* добавления VLAN в список разрешенных, на указанные транки

Шаблон надо создавать вручную, скопировав части конфига в соответствующий шаблон.

Если VLAN необходимо добавить как access, надо настроить и режим интерфейса и добавить его в VLAN:
interface Gi0/1
 switchport mode access
 switchport access vlan 5

Для транков, необходимо только добавить VLAN в список разрешенных:
interface Gi0/10
 switchport trunk allowed vlan add 5

Имена переменных надо выбрать на основании примера данных,
в файле data_files/add_vlan_to_switch.yaml.


Проверьте шаблон templates/add_vlan_to_switch.txt на данных в файле data_files/add_vlan_to_switch.yaml, с помощью функции generate_config из задания 21.1.
Не копируйте код функции generate_config.

vlan_id: 10
name: Marketing
access:
  - Fa0/1
trunk:
  - Fa0/23
  - Fa0/24

router ospf {{ process }}
 router-id {{ router_id }}
 auto-cost reference-bandwidth {{ ref_bw }}
 {% for int in ospf_intf %}
 network {{ int.ip }} 0.0.0.0 area {{ int.area }}
  {% endfor %}
 {% for int in ospf_intf %}
 {% if int.passive == True: %}
 passive-interface {{ int.name }}
 {%endif%}
 {% endfor %}
!
{% for int in ospf_intf %}
{% if int.passive == False: %}
interface {{ int.name }}
 ip ospf hello-interval 1
!
 {%endif%}
 {% endfor %}


"""


from jinja2 import Environment, FileSystemLoader
import yaml
from task_21_1 import generate_config

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/21_jinja2/"
    data_file = "data_files/add_vlan_to_switch.yaml"
    with open(path + data_file) as f:
        info = yaml.safe_load(f)
    print(generate_config('templates/add_vlan_to_switch.txt', info))