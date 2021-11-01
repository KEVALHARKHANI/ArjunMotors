import paramiko
hostname = "192.168.0.103"
port = 8000
myuser = "EDITH"
password = '0000'

sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error
sshcon.connect(hostname=hostname,username= myuser,password=password) # no passwd needed
stdin, sout, stderr = sshcon.exec_command('set /p id="Enter ID: ";echo %id%')
stdin.write('123')
stdin.write('\n')
stdin.flush()
print(sout.readline())

"""for line in iter(sout.readline, ""):
    print(line, end="")"""
print('finished.')
sshcon.close()