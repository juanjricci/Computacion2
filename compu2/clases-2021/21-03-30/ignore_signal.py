import os
import time
import signal

signal.signal(signal.SIGINT,signal.SIG_IGN) # ignora la senal SIGINT (ctrl+C)
print('soy el padre', os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
	time.sleep(10)
	print ('soy el padre')

else:
	print ('soy el hijo')
