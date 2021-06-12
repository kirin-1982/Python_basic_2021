#! /user/bin/env python3

import re
import os
import time
import paramiko
import socket
import getpass
from datetime import datetime

username = input('Username: ')
password = getpass.getpass('Password: ')
now = datetime.now()
date = f'{now.month}-{now.day}-{now.year}'
time_now = f'{now.hour}:{now.minute}:{now.second}'

switch_authentication_failed = []
switch_not_reachable = []
total_number_of_up_ports = 0

with open('ip_list.txt') as iplist:
    number_of_switch = len(iplist.readlines())

total_number_of_ports = number_of_switch * 16

with open('ip_list.txt') as iplist:
    for line in iplist.readlines():
        ip = line.strip()
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip,username=username,password=password)
            print('successfully connect to switch '+ ip)
            command = ssh_client.invoke_shell()
            command.send('term len 0 \n')
            command.send('show ip int b | in up \n')
            time.sleep(1)
            output = command.recv(65535).decode('ascii')
            search_up_ports = re.findall(r'Ethernet\d/\d', output)
            number_of_up_ports = len(search_up_ports)
            total_number_of_up_ports += number_of_up_ports
        except paramiko.ssh_exception.AuthenticationException:
            print('Authentication failed for switch' + ip)
            switch_authentication_failed.append(ip)
        except socket.error:
            print('switch '+ ip + ' is not reachable')
            switch_not_reachable.append(ip)

print('There are totally ' + str(total_number_of_ports) + ' ports available in the network')
print(str(total_number_of_up_ports) + ' ports are currently up')
print('port up rate is %.2f%%' % (total_number_of_up_ports / float(total_number_of_ports) * 100))
print(switch_not_reachable)
print(switch_authentication_failed)

with open(date + '.txt' , 'a+') as f:
    f.write('As of ' + date + ' ' + time_now)
    f.write('\n\n There are totally' + str(total_number_of_ports) + " available ports in the network")
    f.write(' There are ' + str(total_number_of_up_ports) + ' ports are currently up')
    f.write('\n************************************************************\n\n')





