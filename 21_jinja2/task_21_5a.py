# -*- coding: utf-8 -*-
"""
Задание 21.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки
VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.
src_device_params, ,
Для этого задания нет теста!
"""
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import yaml
import os
import re

regex = (r'Tunnel(\d+)')

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    with ConnectHandler(**src_device_params) as ssh:
        ssh.enable()
        command = "sh ip int br"
        output1 = ssh.send_command(command)
    match = re.findall(regex, output1)
    src_tun = (max(match))
    #print(src_tun)
    with ConnectHandler(**dst_device_params) as ssh:
        ssh.enable()
        command = "sh ip int br"
        output2 = ssh.send_command(command)
    match = re.findall(regex, output2)
    dst_tun = (max(match))

    if src_tun >= dst_tun:
        tunnel = int(src_tun) + 1
    else:
        tunnel = int(dst_tun) + 1
    template_dir, template1_file = os.path.split(src_template)
    template_dir, template2_file = os.path.split(dst_template)
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/21_jinja2/"
    for key, value in vpn_data_dict.items():
        vpn_data_dict["tun_num"] = tunnel
    env = Environment(loader=FileSystemLoader(path + template_dir), trim_blocks=True, lstrip_blocks=True)
    template1 = env.get_template(template1_file)
    template2 = env.get_template(template2_file)
    out1 = template1.render(vpn_data_dict)
    out2 = template2.render(vpn_data_dict)
    return out1, out2

if __name__ == "__main__":
    data = {
        "tun_num": None,
        "wan_ip_1": "192.168.100.1",
        "wan_ip_2": "192.168.100.2",
        "tun_ip_1": "10.0.1.1 255.255.255.252",
        "tun_ip_2": "10.0.1.2 255.255.255.252",
    }
    src_device_params = {
        "device_type": "cisco_ios",
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco"
                        }
    dst_device_params = {
        "device_type": "cisco_ios",
        "ip": "192.168.100.2",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco"
                        }
    print(configure_vpn(src_device_params, dst_device_params, 'templates/gre_ipsec_vpn_1.txt', 'templates/gre_ipsec_vpn_2.txt', data))

# хотел еще паралельно зайти на девайси, но уже поздно)