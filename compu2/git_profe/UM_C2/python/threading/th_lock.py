import threading
import time

def f(l, n):
    l.acquire() #----------------------------
    for i in range(3):
        print ("hello world %d %d" % (n,i))
        time.sleep(1)
    l.release() #----------------------------


def f_with(l,n):
    """Ejemplo con with, se llama al acquire cuando se entra al bloque, y al release cuando se sale"""
    with l: # si el recurso está ocupado (acquire usado por otro hilo) me quedo colgado acá
        # esto lo hago si pude hacer el acquire()
        for i in range(3):
            print ("hello world %d %d" % (n,i))
            time.sleep(1)

     #al salir del bloque hago release del lock

if __name__ == '__main__':
    lock = threading.Lock()

    for num in range(2):
        threading.Thread(target=f, args=(lock, num)).start()

    for num in range(2):
        threading.Thread(target=f_with, args=(lock, num)).start()


"""
with open(asdfasfsaf) as fd:
    fd como archivo

afuera del bloque el archivo está cerrado

Equivale a:
fd = open(asdfasf)
fasdfafsa
fd.close()

"""
