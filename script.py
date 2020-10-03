import paramiko
import time
f = open("credentials", "r")
password = (f.read())
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.80.4', port=22, username='', password='')

channel = client.get_transport().open_session()
channel.invoke_shell()

while channel.recv_ready():
    channel.recv(1024)

print(password)
channel.sendall("admin\n")
channel.sendall(password + "\n")
time.sleep(1)
channel.sendall("set interface eth1 type access untag 150\n")
print(channel.recv(1024))