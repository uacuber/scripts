from netmiko import ConnectHandler
import yaml
from concurrent.futures import ThreadPoolExecutor
import logging
import re
import time
import datetime


def send_to_device(device):
    with ConnectHandler(**device) as ssh:
        path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/20_concurrent_connections/"
        ssh.enable()
        device_name = device['ip']                                              # go to out
        now_time = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        prompt = ssh.find_prompt()
        bckp = ssh.send_command('show run')
        with open(path+ (device_name + '_' + now_time + '.txt'), 'w') as bckp_f:
            bckp_f.write(bckp)                                                  # create file|files
        cdp_on = ssh.send_command('show cdp neig')
        if 'CDP is not' in cdp_on:
            out_cdp = 'CDP is OFF'                                              # go to out or not if CDP ON
        else:
            cdp_check = ssh.send_command('show cdp neig deta').split('\n')
            cdp_qty = 0
            for line in cdp_check:
                if '-------------------------' in line:
                    cdp_qty += 1
            out_cdp = 'CDP is ON, ' + str(cdp_qty) + ' peers'                    # go to out
        sh_hard = ssh.send_command('show ver | inc bytes of memory')
        regex_hard = (r'\S+ (\S+) (\S+) .+')
        match_hard = re.search(regex_hard, sh_hard)
        out_dev_type = match_hard.group(1)                                       # go to out
        if 'NPE' in match_hard.group(2):
            out_npe_pe = 'NPE'                                                   # go to out
        else:
            out_npe_pe = 'PE'
        sh_soft = ssh.send_command('show ver | inc Cisco IOS Software')
        regex_soft = (r'Version (.+)')
        match_soft = re.search(regex_soft, sh_soft)
        out_soft = (match_soft.group(1)).replace(', ', '_').replace(' ', '_')    # go to out
        ntp_ip = '192.168.100.2'
        ping_ntp = ssh.send_command(f'ping {ntp_ip}')
        if '!!!' in ping_ntp:                                                    #check NTP, first packets can be lost
            cfg_gmt_ntp = ssh.send_config_set(['clock timezone GMT +0', f'ntp server {ntp_ip}'])

        else:
            print(f'NTP server {ntp_ip} unreachable, pls check or cfg another IP')
            cfg_gmt_ntp = ssh.send_config_set('clock timezone GMT +0')
        time.sleep(1)
        ntp_check = ssh.send_command('show ntp stat')
        if 'unsynchronized' in ntp_check:
            out_ntp = 'Clock in Unsync'                                         # go to out
        else:
            out_ntp = 'Clock in Sync'
        print(device_name + '|' + out_dev_type + '|' + out_soft + '|' + out_npe_pe + '|' + out_cdp + '|' + out_ntp)

def send_to_executor(devices, limit=3):
    with ThreadPoolExecutor(limit) as executor:
        result = executor.map(send_to_device, devices)
        pass

if __name__ == "__main__":
    path = "/home/vagrant/my_repo/online-8-oleg-bosyuk/exercises/20_concurrent_connections/"
    with open(path + "devices2.yaml") as f:
        devices = yaml.safe_load(f)
    send_to_executor(devices)
