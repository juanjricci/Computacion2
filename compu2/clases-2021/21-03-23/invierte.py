import sys

leido = sys.stdin
for line in leido:
    if 'q' == line.rstrip():
        sys.exit(0)
    for word in line.split():
        sys.stdout.write(word[::-1])
        sys.stdout.write(" ")
    sys.stdout.write("\n")