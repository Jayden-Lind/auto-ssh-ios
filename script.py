import paramiko
import time
import os
f = open("./ruckus-creds", "r")
password = (f.read())
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.80.4', port=22, username='', password='')

channel = client.get_transport().open_session()
channel.invoke_shell()

while channel.recv_ready():
    channel.recv(1024)
time.sleep(1)
channel.sendall("admin\n")
channel.sendall(password + "\n")
time.sleep(1)
channel.sendall("set interface eth1 type access untag 35\n")
time.sleep(1)
print(channel.recv(1024))