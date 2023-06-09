#!/usr/bin/python3

import concurrent.futures
import socket
import os

def servicio(s2, addr):
    print (addr)
    enviado = s2.recv(1024)
    respuesta = enviado.decode().upper()
    s2.send(respuesta.encode())
    print (enviado.decode())
    s2.close()

with concurrent.futures.ThreadPoolExecutor() as executor:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(("127.0.0.1",5000))
        s.listen(1)
        while True:
            s2, addr = s.accept()
            result = executor.submit(servicio, s2, addr)
            #s2.close()

