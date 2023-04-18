#!/usr/bin/python3

import time, argparse, signal, sys, os

hijos = list()

def handler_sigusr1(signum, frame):
    for i in hijos:
        os.waitpid(i, 0)
    os.execv('/usr/bin/ps', ['/usr/bin/ps', '-f'])
    raise OSError("Couldn't find/run ps -f")

def main():
    # Set handler
    signal.signal(signal.SIGUSR1, handler_sigusr1)

    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help="Number of children")
    args = parser.parse_args()
    print(f"PID: {os.getpid()}")

    for i in range(args.n):
        hijo = os.fork()
        hijos.append(hijo)
        # Evitar que los hijos hagan fork()
        if hijo == 0:
            break

    # Code for parent
    if hijo > 0:
        while True:
            print("Durmiendo por 5 segundos")
            time.sleep(5)
    
    # Code for child
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()