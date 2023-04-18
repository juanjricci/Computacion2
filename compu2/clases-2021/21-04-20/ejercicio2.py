!#/usr/bin/python3
import os
import multiprocessing as mp
import argparse

STDIN = 0
STDOUT = 0
CHILDNO = 3

# Objetivo de hijos - Lee del pipe y escribe a un archivo
def read_and_dump(pipe, file_name, childno, chunk_sz):
    fd = os.open(f'{file_name}-h{childno}.txt',
                 os.O_RDWR | os.O_CREAT)
    while True:
        chunk = pipe.recv()
        os.write(fd, chunk)
        if len(chunk) < chunk_sz:
            break
    pipe.close()
    return

if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', help='archivo a leer')
    parser.add_argument('-n', help='Size de cada bloque a leer')
    args = parser.parse_args()

    # Abrir el archivo y definir el chunk size (tamano del bloque)
    fd = os.open(f'{args.file}', os.O_RDWR | os.O_CREAT)
    chunk_sz = int(args.n)

    # Array de hijos y pipes de escritura
    child_list = list()
    pipe_list = list()

    # Crear hijos y sus respectivos pipes
    print('Creando hijos...')
    for i in range(CHILDNO):
        parent_pipe, child_pipe = mp.Pipe()
        pipe_list.append(parent_pipe)
        child_list.append(mp.Process(target=read_and_dump, 
                                    args=(child_pipe, 
                                         args.file.replace('.txt', ''),
                                         i , chunk_sz)))

    # Inicializar hijos
    for i in child_list:
        i.start()

    # Leer el archivo y escribir al pipe de a chunks
    print('Leyendo archivo...')
    while True:
        chunk = os.read(fd, chunk_sz)
        for i in pipe_list:
            i.send(chunk)
        if len(chunk) < chunk_sz:
            break

    # Esperar a que terminen los hijos
    for i in child_list:
        i.join()

    print('Copia exitosa!')

    # Cerrar lo usado
    os.close(fd)
    child_pipe.close()
    for i in pipe_list:
        i.close()
