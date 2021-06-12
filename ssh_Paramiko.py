#! /user/bin/env python3
# coding = utf-8

import paramiko
import time

ip = '192.168.245.13'
username = 'python'
password = '123'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=password)

print('successfully connected to ' + ip)
command = ssh_client.invoke_shell()
command.send('config ter\n')
command.send('interface loop1\n')
command.send('ip add 3.3.3.3 255.255.255.255\n')
command.send('end\n')
command.send('wr mem\n')

time.sleep(2)
output = command.recv(65535)
print(output.decode('ascii'))
ssh_client.close()