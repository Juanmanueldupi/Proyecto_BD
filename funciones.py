import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect("%","usuario","usuario","dasedatos_anime")
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

#0. Listar el numero de estudios y su nombre.


def Listar_animes(db):
    sql="SELECT * FROM Anime"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existen animes en la base de datos.")
        else:    
            animes = cursor.fetchall()
            #print("Tabla de animes")
            for anime in animes:
                print(anime)
    except:
        print("Error al consultar los datos.")

#1. Pide por teclado un estudio y te informa del anime(o animes) que produce.

def listar_animes_estudio(db,estudio):
    sql="select * from Anime where estudio ="+estudio
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       for registro in registros:
          print(registro["titulo"]," --- ",registro["isbn"]," --- ",registro["estudio"]," --- ",registro["fecha"]," --- ","Precio:",registro["precio"])
    except:
       print("Error en la consulta")



#2. Inserta un nuevo anime.



#3. Elimina los animes de un estudio.

#4. Empiezan las rebajas, pide un genero por teclado y rebaja los animes que sean de ese genero un 10%.



#Desconectar 
def Desconectar_BD(db):
    db.close()
