import sys
import MySQLdb
from funciones import *

try:
    bbdd= MySQLdb.connect("localhost","usuario","usuario","basedatos_anime")
except MySQLdb.Error as e:
    print("No puedo conectar a la base de datos:",e)
    sys.exit(1)
print("Conexión establecida.")


opcion=MostrarMenu()

while opcion != 0:
    if opcion == 1:
        print(Contar_estudios(bbdd))
        print(Listar_estudios(bbdd))
    elif opcion == 2:
        estudio=input("Introduce el nombre de un estudio para comprobar sus producciones : ")
        print(listar_animes_estudio(bbdd,estudio))
    elif opcion == 3:
        anime={}
        anime["titulo"]=(input("Introduce el titulo: "))
        anime["isbn"]=input("Introduce el isbn (13 numeros): ")
        anime["estudio"]=input("Introduce el estudio: ")
        anime["genero"]=input("Introduce el genero (Supernatural,Seinen,Romance,Shonen,Action): ")
        anime["fecha"]=input("Introduce la fecha (año-mes-dia): ")
        anime["precio"]=input("Introduce el precio(9999.99):")
        print(Insertar_BD(bbdd,anime))
        print("Insercion realizada correctamente")
    elif opcion == 4:
        print(Listar_estudios(bbdd))
        nombre_estudio=input("Introduce el estudio cuyos animes quieras eliminar: ")
        Borrar_BD(bbdd,nombre_estudio)
        print(Listar_animes(bbdd))
    elif opcion==5:
        genero=input("Introduce un genero (Supernatural,Seinen,Romance,Shonen,Action):")
        print(Rebajas(bbdd,genero))
    else:
        print("Opción incorrecta.")
    
    opcion=MostrarMenu()
    
Desconectar_BD(bbdd)
