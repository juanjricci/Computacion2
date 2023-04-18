#!/usr/bin/python

from os import fork

def main():
    fork()
    fork()
    fork()
    print("hola mundo")


if __name__ == "__main__":
    main()
