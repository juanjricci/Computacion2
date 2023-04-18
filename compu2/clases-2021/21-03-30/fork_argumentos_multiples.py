#!/usr/bin/python3

import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Nivel de output del programa")
    parser.add_argument("c", type=int, help="Cantidad de hijos que se utilizaran", default=1)

    args = parser.parse_args()

    if args.verbose:
        print("MODO VERBOSO")
        print(f"PID del padre: {os.getpid()}")
        print("Creando hijo...")

    for i in range(args.c):
        hijo = os.fork()

        if hijo > 0: # Nos encontramos en el padre
            os.waitpid(hijo, 0)

        elif hijo == 0: # Nos encontramos en el hijo
            n = float(input("\tIngrese el 1er valor: "))
            m = float(input("\tIngrese el 2do valor: "))
            resultado = 0.5 * (n + m)
            if args.verbose:
                print(f"\tPID del hijo: {os.getpid()}")
                print(f"\tEl promedio entre {n} y {m} es: {resultado}")
                print(f"\tMi padre es {os.getppid()}")
                print("Terminando el hijo")
            else:
                print(f"{resultado}")
            sys.exit(0)
    
    if args.verbose:
        print("Terminando el padre")
    sys.exit(0)

if __name__ == "__main__":
    main()