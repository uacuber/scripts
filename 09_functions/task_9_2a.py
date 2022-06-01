# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря
trunk_config и шаблона trunk_mode_template.

    for key, value in zip(key, value):
        result_dict[key] = [value]
        print(result_dict)

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    dict_out = {}
    for int in intf_vlan_mapping:
        command_out = []
        for command in trunk_template:
            if 'allowed v' in command:
                vlan_found = (str(intf_vlan_mapping[int]).strip('[]')).split()
                command_out.append(command + ' '+ ''.join(vlan_found))
            else:
                command_out.append(command)
        dict_out[int] = command_out
    return(dict_out)

generate_trunk_config(trunk_config, trunk_mode_template)




