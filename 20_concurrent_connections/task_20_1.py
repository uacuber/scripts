# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor


def ping_ip_addres(ip):
    result = subprocess.run(
        ["ping", "-c", "3", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        return (ip, True)
    else:
        return (ip, False)

def ping_ip_addresses(ip_list, limit=3):
    list_alive = []
    list_dead = []
    with ThreadPoolExecutor(limit) as executor:
        result = executor.map(ping_ip_addres, ip_list)
        for ip, value in result:
            if value:
                list_alive.append(ip)
            else:
                list_dead.append(ip)
        print(list_alive, list_dead)
        return list_alive, list_dead

if __name__ == "__main__":
    ip_list = ['8.8.8.8', '8.1.4.4']
    ping_ip_addresses(ip_list)