import os
import time
import signal

def manejador(nro, frame):
	print('llego la senal', nro)
	print('segur que quiere terminar el programa?')
	signal.signal(signal.SIGINT,signal.SIG_DFL)

signal.signal(signal.SIGINT,manejador) # maneja la senal SIGINT (ctrl+C)
print('soy el padre', os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
	time.sleep(10)
	print ('soy el padre')

else:
	print ('soy el hijo')
