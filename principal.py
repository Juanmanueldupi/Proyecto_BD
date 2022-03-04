from funciones import *
import sys
import MySQLdb

try:
    bbdd= MySQLdb.connect("localhost","arantxa","1234","proyecto_bd")
except MySQLdb.Error as e:
    print("No puedo conectar a la base de datos:",e)
    sys.exit(1)
print ("Conexión establecida.")

menu='''
Menú:
1. 
2. 
3. 
4. 
5.
6. Salir
'''