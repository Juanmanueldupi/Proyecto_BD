import sys
import MySQLdb
from funciones import *

try:
    bbdd= MySQLdb.connect("localhost","usuario","usuario","basedatos_anime")
except MySQLdb.Error as e:
    print("No puedo conectar a la base de datos:",e)
    sys.exit(1)
print("Conexión establecida.")



menu='''
Menú:
0. Listar el numero de estudios y su nombre.
1. Pide por teclado un estudio y te informa del anime(o animes) que produce.
2. Inserta un nuevo anime.
3. Elimina los animes de un estudio.
4. Empiezan las rebajas, pide un genero por teclado y rebaja los animes que sean de ese genero un 10%.
5. Salir
'''



print (menu)
opcion=int(input("Opción: "))