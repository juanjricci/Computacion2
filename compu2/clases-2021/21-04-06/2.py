#!/usr/bin/python3

# este cogigo solo hace la comunicacion entre procesos usando mensjes
#hijo1 -> hijo2 SIGUSR1
#hijo2 -> hijo1 SIGUSR2
#hijo1 -> hijo2 SIGTERM
#hijo2 -> hijo1 SIGTERM
import os
import argparse
import signal
import time

pidh1 = 0 
pidh2 = 0

def modifica_archivo(nro, frame):
    global pidh1
    archivo = open("archivo.txt", 'r')
    salida = ''
    linea = archivo.readline()
    while linea != '':
        salida = salida + rot13(linea)
        linea = archivo.readline()
    archivo.close()
    print("hijo2 reemplazando...")
    archivo = open("archivo.txt", 'w')
    archivo.write(salida)
    archivo.close()
    os.kill(pidh1, signal.SIGUSR2)

def rot13(entrada):
    codec = "abcdefghijklmnopqrstuvwxyz"
    codec2 = codec + codec
    salida = ""
    for caracter in entrada:
        indice = (codec.find(caracter))
        if indice >= 0:
            salida = salida + codec2[indice + 13]
        else:
            salida = salida + caracter
    return salida

def muestra_modificado(nro, frame):
    print("hijo1 leyendo...")
    fd = os.open("archivo.txt", os.O_RDONLY)
    while True:
        leido = os.read(fd, 1024)
        os.write(1, leido)
        if len(leido) == 0:
            break
    os.close(fd)
    # suicidio en masa
    global pidh2
    os.kill(pidh2, signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGTERM)

def termina_hijo(nro, frame):
    exit()

if __name__ == "__main__":
    
    pidh2 = os.fork() # primero creo el hijo 2

    if pidh2 == 0: # hijo 2
        signal.signal(signal.SIGUSR1, modifica_archivo) # si recibe sigusr1 ejecuta modificar_archivo que es la tarea que tiene que hacer el hijo 2
        signal.signal(signal.SIGTERM, termina_hijo) # si le llega sigterm ejecuta termina_hijo()
        signal.pause() # se queda esperando hasta que llegue una senal

    pidh1 = os.fork()

    if pidh1 == 0: # hijo 1
        signal.signal(signal.SIGUSR2, modifica_archivo) # si recibe sigusr2 muestra el archivo modificado
        signal.signal(signal.SIGTERM, termina_hijo) # si le llega sigterm termina
        # este no se puede quedar esperando
        fd = os.open("archivo.txt", os.O_CREAT|os.O_WRONLY|os.O_TRUNC, 440) # abre el archivo. Si no existe lo crea y si existe lo trunca
        print("hijo escribiendo...")
        while True: # va leyendo hasta el fin del archivo
            leido = os.read(0, 1024)
            os.write(fd, leido)
            if len(leido) == 0:
                break
        os.close(fd)
        os.kill(pidh2, signal.SIGUSR1) # le mando sigusr1 a mi hno, el hijo 2 (ahora va a empezar a rabajar el hijo 2)
        signal.pause() # se queda esperando hasta que le llegue una senal
    
    # padre
    signal.signal(signal.SIGUSR2, signal.SIG_IGN)
    os.wait()
    os.wait()
    print("terminando todos los hijos")