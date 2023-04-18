import signal, os
import time

def handler(nro, frame): # nro es el nro de senal (el nro de SIGALRM es 14)
	print('signal handler called with signal', nro)
	signal.alarm(3)

# set the signal handler and a 3-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(1) # espera 1 segundo y tira la senal, luego espera los 3 segundos de la funcion para tirar la otra senal

time.sleep(10)
print('termino el programa')
