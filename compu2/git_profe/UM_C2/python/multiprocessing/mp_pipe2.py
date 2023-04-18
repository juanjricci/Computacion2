
from multiprocessing import Process, Pipe
import os,time

def f(r,w,nproc):
    print("nproc vale: %d" % nproc)
    if(nproc == 2):
        print("receptor")
        print("%d: proc %d recibiendo: %s" % (nproc, os.getpid(),r.recv()))
        r.send("_hello world")
    if(nproc == 1):
        print("emisor")
        w.send("proc %d enviando" % (os.getpid()))
        print(str(nproc) + w.recv())
    r.close()
    w.close()
    print("Proceso PID %d (%d) terminando..." % (os.getpid(), nproc))

if __name__ == '__main__':
    r, w = Pipe()
    print("padre: %d" %os.getpid())
    p1 = Process(target=f, args=(r,w,1))
    p2 = Process(target=f, args=(r,w,2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Bye...")
