import os, time, sys


pipe_name = '/tmp/pipe_test'

def lector( ):
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time( )))

# inicio del codigo
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)  


lector()
