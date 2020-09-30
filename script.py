import base64
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.80.4', username='admin', password='')
stdin, stdout, stderr = client.exec_command('')
stdin.write('\n')
stdin.write('admin\n')
stdin.write('\n')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()