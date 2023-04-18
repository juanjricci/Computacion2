import socket

# creo el socket (tipo INET y TCP - {AF_INET Y SOCK_STREAM respectivamente})
# esto va a ser un fd (file descriptor)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# en este print puedo ver q se trata de un fd
print(s)

# aca le digo donde me quiero conectar (direccion ip o nombre y puerto)
# esto hace el handshake para la conexion
s.connect(("juncotic.com", 80))

# le mando un dato
s.send(b"get /http /1.1 \r\n\r\n")

# espero la respuesta (la recibo)
respuesta = s.recv(2048)

# imprimo la respuesta para ver que me devolvio
print(respuesta.decode())

# el servidor al no recibir nada cierra la conexion mandandome un finish
# le mando el finish al servidor (aunq esto ya no hace falta pq la conexion ya cierra al terminar de ejecutar el programa)
s.close()