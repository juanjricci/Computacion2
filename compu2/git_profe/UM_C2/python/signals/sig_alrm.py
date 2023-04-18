#!/usr/bin/python
import signal, os

#def handler(signum, frame):
#    print('Signal handler called with signal', signum)

def handler():
    print('Signal handler called with signal')


def main():
    signal.signal(signal.SIGALRM, handler)

    print("Antes del alarm")
    signal.alarm(5)
    print("Despues del alarm, antes del pause")
    signal.pause()
    print("Despues del pause")
    
    signal.alarm(0)          # Disable the alarm

if __name__ == "__main__":
    main()

