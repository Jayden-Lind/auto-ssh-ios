import paramiko
import time
import os
import re
import sys
f = open("./ruckus-creds", "r")
password = (f.read())
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.80.4', port=22, username='', password='')
channel = client.invoke_shell()
time.sleep(1)
channel.send("admin\n")
time.sleep(1)
channel.send(password + "\n")
time.sleep(1)
channel.send("set interface eth1 type access untag 35\n")
time.sleep(1)
tmp = str(channel.recv(65535).decode(encoding='utf-8'))
xe = re.findall('^OK' , tmp,re.MULTILINE)
if xe:
    sys.exit("Successful")
    exit(0)
else:
    sys.exit("Failure")
    exit(1)