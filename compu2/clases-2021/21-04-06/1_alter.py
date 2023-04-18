#!/usr/bin/python3

import argparse
import os
import signal

def handler(nro, stack):
    global cantidad
    for i in range(cantidad):
        os.wait()
    os.execlp("ps", "/usr/bin/ps", "-f") # a partir de este punto cambia su cuerpo por ps -f
    # cualq codigo
    # q este aca
    # nunca se va
    # a ejecutar

print(f"PID: {os.getpid()}")

signal.signal(signal.SIGUSR1, handler)

parser = argparse.ArgumentParser(description="Ejercicio 1")
parser.add_argument('-n', '--nro', action="store_true", default=False, help='nro')
parser.add_argument('cantidad', type=int, help="Cantidad de zombies", metavar='nro')

args = parser.parse_args()
cantidad = args.cantidad

if args.nro != True:
    exit(0)

for i in range(cantidad):
    pid = os.fork()
    # esto lo ejecuta el hijo
    if pid == 0:
        exit(0) # si es el hijo termina

# si es el padre pasa esto
leido = input("cualquier tecla termina...")