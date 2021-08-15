import paramiko
import time
import re
import sys
if sys.argv[1]:
    vlan = int(sys.argv[1])
else:
    vlan = '35'

with open("./ruckus-creds", "r") as password:
    password = (password.read())
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.80.4', port=22, username='admin', password=password)
channel = client.invoke_shell()
time.sleep(1)
channel.send("admin\n")
time.sleep(1)
channel.send(password + "\n")
time.sleep(1)
channel.send(f"set interface eth1 type access untag {vlan}\n")
time.sleep(1)
recieve_channel = str(channel.recv(65535).decode(encoding='utf-8'))


if re.findall('^OK' , recieve_channel,re.MULTILINE):
    sys.exit("Successful")
else:
    sys.exit("Failure")