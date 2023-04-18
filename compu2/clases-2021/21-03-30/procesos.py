import os

print ('pid: ', os.getpid(), 'bash ppid: ',os.getppid())
pid = os.fork()
if (pid == 0):
	os.execlp('ps', 'ps', '-f')
else:
	print ('Padre, pid: ', os.getpid(), 'ppid: ',os.getppid())
