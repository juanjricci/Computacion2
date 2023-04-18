import threading, time

NTHREADS=5 # numero de threads
NITER=1000000 # numero de iteraciones

contador=0

def count(i_hilo,l):
    global contador
    local=0

    for i in range(NITER):
        # INI seccion critica
        l.acquire()
        tmp = contador
        tmp = tmp+1
        contador = tmp
        l.release()
        # FIN seccion critica

        local +=1

    print(f"Hilo {i_hilo} cicló {local} veces")


"""
contador = 1000

Hilo 0                          
contador?                       
    contador vale 1000         
debo sumar 1000+1 = 1001        
-->                            Hilo 1
                                contador?
                                    contador vale 1000
                                debo sumar 1000+1 = 1001
                                almaceno: contador = 1001
                                <---
almaceno: contador = 1001


"""



hilos = []
lock = threading.BoundedSemaphore(1)

# creamos NTHREADS hilos
for i in range(NTHREADS):
    hilos.append(threading.Thread(target=count, args=(i,lock)))
    hilos[-1].start()

# esperamos a que los NTHREADS hilos terminen
for i in range(NTHREADS):
    hilos[i].join()

# hilos terminados

if (contador != NTHREADS*NITER):
    print("NOOOOOO! contador es [%d] y deberia ser %d" % (contador, NITER*NTHREADS))
else:
    print("Bien!! contador vale %d" % contador)


