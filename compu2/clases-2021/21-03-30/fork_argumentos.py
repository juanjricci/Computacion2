import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Nivel de output del programa")
    parser.add_argument("n", type=float, help="1er Numero")
    parser.add_argument("m", type=float, help="2do Numero")

    args = parser.parse_args()

    if args.verbose:
        print("MODO VERBOSO")
        print(f"PID del padre: {os.getpid()}")
        print("Creando hijo...")

    hijo = os.fork()

    if hijo > 0: # Nos encontramos en el padre
        os.waitpid(hijo, 0)
        if args.verbose:
            print("Terminando el padre")
        sys.exit(0)
    elif hijo == 0: # Nos encontramos en el hijo
        resultado = 0.5 * (args.n + args.m)
        if args.verbose:
            print(f"\tPID del hijo: {os.getpid()}")
            print(f"\tEl promedio entre {args.n} y {args.m} es: {resultado}")
            print(f"\tMi padre es {os.getppid()}")
            print("Terminando el hijo")
        else:
            print(f"{resultado}")
        sys.exit(0)

if __name__ == "__main__":
    main()