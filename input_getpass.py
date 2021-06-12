#! /user/bin/env python3

from getpass import getpass
import paramiko
import time


username = input("Username: ")
password = getpass("Password: ")

for i in range(11, 16):
    ip = '192.168.245.' + str(i)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(username=username, password=password,hostname=ip)
    print('successfully connected to switch ' + ip)
    command = ssh_client.invoke_shell()
    command.send('configure terminal\n')
    for vlan_id in range(10,21):
        print('Creating VLAN ' + str(vlan_id))
        command.send('vlan ' + str(vlan_id) + '\n')
        command.send('name Python_VLAN ' + str(vlan_id) + '\n')
        time.sleep(1)
    command.send('end\n')
    command.send('wr\n')
    time.sleep(2)
    output = command.recv(65535)
    print(output.decode('ascii'))
    ssh_client.close()
