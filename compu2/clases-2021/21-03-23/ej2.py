

archivo_origen = input('Archivo origen: ')
archivo_destino = input('Archivo destino: ')

destino = open(archivo_destino, "w")
with open(archivo_origen, "r") as origen:
    data = origen.read()
    destino.write(data)

destino.close()
origen.close()