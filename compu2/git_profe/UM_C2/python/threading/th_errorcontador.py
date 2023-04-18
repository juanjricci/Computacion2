import threading, time

NTHREADS=6 # numero de threads
NITER=1000000 # numero de iteraciones

contador=0

def count():
    global contador
    for i in range(NITER):
        tmp = contador
        tmp = tmp+1
        contador = tmp


hilos = []
for i in range(NTHREADS):
    hilos.append(threading.Thread(target=count, ))
    hilos[-1].start()


for i in range(NTHREADS):
    hilos[i].join()

if (contador != NTHREADS*NITER):
    print("NOOOOOO! contador es [%d] y deberia ser %d" % (contador, NITER*NTHREADS))
else:
    print("Bien!! contador vale %d" % contador)


