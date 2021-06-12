#! /user/bin/env python3

import paramiko
import time
from getpass import getpass


username = input('Username: ')
password = getpass('Password: ')

with open('ip_list.txt', 'r') as f:
    for line in f.readlines():
        ip  = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(username=username, password=password,hostname=ip)
        print('successfully connected to switch ' + ip)
        command = ssh_client.invoke_shell()
        command.send('configure terminal \n')
        command.send('file prompt quiet \n')
        command.send('end\n')
        command.send('copy running-config ftp://python:python@192.168.245.101 \n')
        command.send('wr\n')
        time.sleep(1)
        output = command.recv(65535)
        print(output.decode('ascii'))
        print('backup finished for switch '+ ip)
        ssh_client.close()
