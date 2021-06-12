#! /user/bin/env python3

from netmiko import ConnectHandler
import json

sw2 = {
    'device_type' : 'cisco_ios',
    'ip': '192.168.245.11',
    'username': 'python',
    'password' : '123'

}

conn = ConnectHandler(**sw2)
print('Successfully connected to ' + sw2['ip'])
interfaces = conn.send_command('show ip int brief', use_textfsm=True)   # Test ntc-template module
print(interfaces)
for interface in interfaces:
    if interface["status"] == 'up' and interface["ipaddr"] != 'unassigned':
        print(f'{interface["intf"]} is up, ip address is {interface["ipaddr"]}')



