# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""

'''
path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/21_jinja2/"
env = Environment(loader=FileSystemLoader(path + "templates"), trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template("for.txt")

with open(path + 'data_files/' + 'for.yml') as f:
    info = yaml.safe_load(f)

out = (template.render(info))
print(out)
'''
'''


def generate_config(template, data_dict):
    env = Environment(loader=FileSystemLoader(path), trim_blocks=True,
    lstrip_blocks=True)
    template = env.get_template(template)
    out = template.render(info)
    return out
'''

from jinja2 import Environment, FileSystemLoader
import yaml
import os

def generate_config(template, data_dict):
    template_dir, template_file = os.path.split(template)
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/21_jinja2/"
    env = Environment(loader=FileSystemLoader(path + template_dir),trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_file)
    out = template.render(data_dict)
    return out

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/21_jinja2/"
    data_file = "data_files/for.yml"
    with open(path + data_file) as f:
        info = yaml.safe_load(f)
    print(generate_config('templates/for.txt', info))