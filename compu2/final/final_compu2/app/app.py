import psycopg2
from psycopg2 import Error

conn = psycopg2.connect(user="postgres",
                        password="6250",
                        host="127.0.0.1",
                        port="5432",
                        database="compu2")

cur = conn.cursor()

legajo = input("Ingrese su legajo")

cur.execute(f'SELECT nombre, apellido FROM polls_alumnos where id = {legajo}')

algo = cur.fetchone()

print(algo)