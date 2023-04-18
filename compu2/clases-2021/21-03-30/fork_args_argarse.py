#!/usr/bin/python3

import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-n', nargs=1, type=int, required=True, help='Primer numero')
parser.add_argument('-m', nargs=1, type=int, required=True, help='Segundo numero')
parser.add_argument('-v', action="store_true", help='modo verboso')
args = parser.parse_args()

pid = os.fork()

if pid > 0:
    if args.v:
        print('Modo verboso...')
        print('PID padre: ', os.getpid())
else:
    promedio = (args.n[0] + args.m[0])/2
    if args.v:
        print('Creando hijo...')
        print('PID hijo: '+ str(os.getpid()) + 'promedio: ' + str(promedio))