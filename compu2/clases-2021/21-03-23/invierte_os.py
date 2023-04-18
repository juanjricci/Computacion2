import os

while True:
    leido = os.read(0, 1024)
    for line in leido.splitlines():
        for word in line.split():
            os.write(1, (word[::-1] + bytes(" ", "utf-8")))
        os.write(1, b"\n")
    if len(leido) != 1024:
        break