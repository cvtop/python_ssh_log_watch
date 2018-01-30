import time
import winsound
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
while True:
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	ssh.connect('10.122.25.145', username = 'appadmin', password = 'passw0rd', timeout = 300)
	cmd = 'ls -l /tmp/work/hana_disk/watch.log; cat /tmp/work/hana_disk/watch.log'
	stdin, stdout, stderr = ssh.exec_command(cmd)
	#ssh.close()
	out=stdout.readlines()
	for o in out:
		if 'FATAL' in o:
			print o
			winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
		else:
			print o
	###time sleep
	time.sleep(30)


