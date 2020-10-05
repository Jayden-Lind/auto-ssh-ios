import paramiko
import time
import os
f = open("./ruckus-creds", "r")
password = (f.read())
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.80.4', port=22, username='', password='')

channel = client.invoke_shell()

time.sleep(1)
channel.send("admin\n")
time.sleep(1)
print(channel.recv(65535).decode(encoding='utf-8'))
channel.send(password + "\n")
time.sleep(1)
print(channel.recv(65535).decode(encoding='utf-8'))
channel.send("set interface eth1 type access untag 35\n")
time.sleep(1)
print(channel.recv(65535).decode(encoding='utf-8'))