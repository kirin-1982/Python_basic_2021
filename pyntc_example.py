#! /user/bin/env python3

import json
from pyntc import ntc_device as NTC
import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')


with open('ip_list.txt') as f:
    for sw in f.readlines():
        ip = sw.strip()
        ssh_conn = NTC(host=ip, username=username, password=password, device_type='cisco_ios_ssh')
        print('Successfully connect to switch '+ str(ip))
        ssh_conn.open()
        file_name = str(ip) + '_running-config.cfg'
        ssh_conn.backup_running_config(file_name)
        print('Successfully backup the running config to ' + file_name)
        ssh_conn.close()

# print(json.dumps(sw1.facts, indent=4))
# print(sw1.running_config)

# sw1.config('hostname pyntc_sw1')
# sw1.close()

