import os

archivo_origen = input('Archivo origen: ')
archivo_destino = input('Archivo destino: ')

fd_origen = os.open(archivo_origen, os.O_RDONLY)
fd_destino = os.open(archivo_destino, os.O_WRONLY | os.O_CREAT)
while True:
    leido = os.read(fd_origen, 1024)
    os.write(fd_destino, leido)
    if len(leido) != 1024:
        break

os.close(fd_origen)
os.close(fd_destino)