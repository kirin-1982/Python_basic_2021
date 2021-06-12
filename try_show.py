#! /user/bin/env python3

import paramiko
import time
from getpass import getpass
import sys
import socket


username = input('Username: ')
password = getpass('Password: ')
ip_file = sys.argv[1]
cmd_file = sys.argv[2]
switch_authentication_failed = []
switch_unreachable = []

with open(ip_file, 'r') as ip_list:
    for ip in ip_list.readlines():
        try:
            ip = ip.strip()
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(username=username, password=password,hostname=ip)
            print('successfully connected to switch ' + ip)
            command = ssh_client.invoke_shell()
            with open(cmd_file, 'r') as cmds:
                for cmd in cmds.readlines():
                    command.send(cmd + '\n')
            time.sleep(2)
            output = command.recv(65535)
            print(output.decode('ascii'))
            ssh_client.close()
        except paramiko.ssh_exception.AuthenticationException:
            print('User authentication failed for ' + ip + '.')
            switch_authentication_failed.append(ip)
        except socket.error:
            print(ip + ' is not reachable')
            switch_unreachable.append(ip)

print('\nUser authentication failed for below switches: ')
for sw in switch_authentication_failed:
    print(sw)
print('\nBelow switches are not reachable:  ')
for sw in switch_unreachable:
    print(sw)
