from multiprocessing import Process, Value, Array

"""
Value: valor en memoria compartida
Array: arreglo en memoria compartida
    i: entero con signo
    d: double
    se puede usar multiprocessing.sharedctypes para tener más flexibilidad
"""


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
