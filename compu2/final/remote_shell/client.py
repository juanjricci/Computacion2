#!/usr/bin/python3

import socket
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

# get local machine name
host = socket.gethostname()
# host = sys.argv[1]

port = 1234  # int(sys.argv[2])

print("Haciendo el connect")
# connection to hostname on the port.
s.connect((host, port))
print("Handshake realizado con exito!")

command = input("Ingrese el legajo: ")

print("Enviando datos al server")
msg = s.send(command.encode())

while (True):
    consulta = input("Tiene otra consulta?[y/n]")
    if consulta == 'y':
        menu = "Elija una opcion\n1. Horarios de cursado.\n"
        opcion = input(menu)
        if opcion == 1:
            op = 'horarios'
            s.send(op.encode())
    else:
        False

print("Reciviendo datos del server")
recv = s.recv(1024)
print(recv.decode())

#print (msg.decode('ascii'))
#print (msg.decode('utf-8'))
s.close()
print("Cerrando conexion")
