import os
import time

print("Soy el padre", os.getpid(), os.getppid())

pid = os.fork()

if pid > 0:
    os.wait()
    print("Soy el padre")
else:
    time.sleep(1)
    print("Soy el hijo")