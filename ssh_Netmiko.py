#! /user/bin/env python3
# coding = utf-8

import netmiko

sw2 = {
    'device_type' : 'cisco_ios',
    'ip': '192.168.245.12',
    'username': 'python',
    'password' : '123'

}

con = netmiko.ConnectHandler(**sw2)
print('successfully connect to ' + sw2['ip'])
config_commands = ['int loop1', 'ip add 2.2.2.2 255.255.255.255']
output = con.send_config_set(config_commands)
print(output)
result = con.send_command('show run int loop1')
print(result)
