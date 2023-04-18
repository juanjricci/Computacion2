#!/usr/bin/python3
import argparse
import sys

def get_header_data(image):
    ppm = open(image, encoding='latin1').read()
    header_data = []
    i = 0
    header_length = 3
    for line in ppm.splitlines():
        header_data.append(line)
        if line.startswith('#'):
            header_length = header_length + 1
        print(line)
        if len(header_data) == header_length:
            break
    return f'largo del encabezado: {sys.getsizeof(header_data)} bytes'
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file',help='imagen',
                        action='store',required=True)
    args = parser.parse_args()
    if args.file:
        imagen = args.file
        print(get_header_data(imagen))

if __name__ == '__main__':
    main()
