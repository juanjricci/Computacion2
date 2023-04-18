#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()

# Grupo mutuamente exclusivo (solo puede estar seleccionado uno)
operations = parser.add_mutually_exclusive_group()
operations.add_argument("-s", "--suma", action="store_true", help="suma arg1 + arg2")
operations.add_argument("-r", "--resta", action="store_true", help="resta arg1 - arg2")
operations.add_argument("-m", "--multi", action="store_true", help="multiplica arg1 * arg2")
operations.add_argument("-d", "--div", action="store_true", help="divide arg1 / arg2")

# Argumento para el tipo de dato
parser.add_argument("-t", "--type", type=str, choices=['int', 'float'], default='float')

# Argumentos numericos
parser.add_argument('arg1', help="Primer operando")
parser.add_argument('arg2', help="Segundo operando")

# Parsear argv a un objeto args
args = parser.parse_args()

# Determinar el tipo de datos con el que se trabajara (int o float)
if args.type == 'float':
    args.arg1 = float(args.arg1)
    args.arg2 = float(args.arg2)
else:
    args.arg1 = int(args.arg1)
    args.arg2 = int(args.arg2)

# Determinar la operacion que se realizara
if args.suma:
    resultado = args.arg1 + args.arg2
    print(f"{args.arg1} + {args.arg2} = ", end='')
elif args.resta:
    resultado = args.arg1 - args.arg2
    print(f"{args.arg1} - {args.arg2} = ", end='')
elif args.multi:
    resultado = args.arg1 * args.arg2
    print(f"{args.arg1} * {args.arg2} = ", end='')
elif args.div:
    resultado = args.arg1 / args.arg2
    print(f"{args.arg1} / {args.arg2} = ", end='')

# Mostrar por pantalla
print(resultado)