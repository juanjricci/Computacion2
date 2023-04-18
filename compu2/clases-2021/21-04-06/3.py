#!/usr/bin/python3
import time
import os
import signal

class Senal():
    def __init__(self):
        self.time = 1
        self.numero = 0
    
    def handler(self, signal_number, frame):
        if signal_number == 10:
            self.time = self.time * 2

        if signal_number == 12:
            self.time = self.time / 2
            if self.time < 1:
                exit()

    def mostrar(self):
        while True:
            self.numero += 1
            print(self.numero)
            time.sleep(self.time)

if __name__ == "__main__":

    senal = Senal()
    def recibir_senal(signal_number, frame):
        senal.handler(signal_number, frame)

    signal.signal(signal.SIGUSR1, recibir_senal)
    signal.signal(signal.SIGUSR2, recibir_senal)

    print(os.getpid())
    senal.mostrar()

    signal.pause() # espera a que llegue una senal
