#!/usr/bin/python3

import sys
import getopt

argv = sys.argv[1:]

opts, args = getopt.getopt(argv, "srmdph")

for opt, arg in opts:
    if not arg and opt == '-h':
        print('Help: use one of this options [-s|-r|-m|-d|-p|-h]')
    if opt == '-s':
        print(int(args[0])+int(args[1]))
    elif opt == '-r':
        print(int(args[0])-int(args[1]))
    elif opt == '-m':
        print(int(args[0])*int(args[1]))
    elif opt == '-d':
        print(int(args[0])/int(args[1]))
    elif opt == '-p':
        print(int(args[0])**int(args[1]))