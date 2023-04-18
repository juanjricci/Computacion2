import sys
import threading
import time
import os


DELAY=1

def thread_function(name):
    print("HILO %d: Este es el hilo: %s (%d)" % (name, threading.current_thread().getName(), threading.current_thread()._ident))
    time.sleep(DELAY)
    print("HILO %d: terminando" % name)


if __name__ == "__main__":

    print("MAIN: Iniciando programa principal, antes de crear el thread_______ mi PID es %d, thread %d" % (os.getpid(), threading.get_ident()))

    x1 = threading.Thread(target=thread_function, args=(1,), daemon=True) 
    x2 = threading.Thread(target=thread_function, args=(2,), daemon=True) 
    
    x1.start()
    x2.start()
  
    print("MAIN: cantidad de threads activos: ", threading.active_count())
    print("MAIN: Este es el hilo: %s (%d)" % (threading.current_thread().getName(), threading.current_thread()._ident))

    for i in threading.enumerate():
        print("Nombre: ", i.getName(), "(",i._ident,", Vivo?: ",i.is_alive(),", Daemon?:",i.isDaemon())

    # hilo principal esperando...
    x1.join()
    x2.join()

    # por acá
    # termina
