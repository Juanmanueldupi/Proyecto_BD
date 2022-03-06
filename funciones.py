import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect("%","usuario","usuario","dasedatos_anime")
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

#Menu

def MostrarMenu():
    menu='''
    1. Listar el numero de estudios y su nombre.
    2. Pide por teclado un estudio y te informa del anime(o animes) que produce.
    3. Inserta un nuevo anime.
    4. Elimina los animes de un estudio.
    5. Empiezan las rebajas, pide un genero por teclado y rebaja los animes que sean de ese genero un 10%.
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")

#1. Listar el numero de estudios y su nombre.


def Contar_estudios(db):
    sql="SELECT count(estudio) FROM Anime"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existen animes en la base de datos.")
        else:    
            animes = cursor.fetchall()
            for anime in animes:
                print(anime)
    except:
        print("Error al consultar los datos.")

def Listar_estudios(db):
    sql="SELECT estudio FROM Anime"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existen animes en la base de datos.")
        else:    
            animes = cursor.fetchall()
            for anime in animes:
                print(anime)
    except:
        print("Error al consultar los datos.")

def Listar_animes(db):
    sql="SELECT titulo FROM Anime"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existen animes en la base de datos.")
        else:    
            animes = cursor.fetchall()
            for anime in animes:
                print(anime)
    except:
        print("Error al consultar los datos.")

def Listar__toda_la_info_animes(db):
    sql="SELECT * FROM Anime"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existen animes en la base de datos.")
        else:    
            animes = cursor.fetchall()
            for anime in animes:
                print(anime)
    except:
        print("Error al consultar los datos.")

#2. Pide por teclado un estudio y te informa del anime(o animes) que produce.

def listar_animes_estudio(db,estudio):
    sql="select * from Anime where estudio = '"+estudio+"'"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       for registro in registros:
          print(registro["titulo"])
#Toda la informacion del anime
#          print(registro["titulo"]," --- ",registro["isbn"]," --- ",registro["estudio"]," --- ",registro["fecha"]," --- ","Precio:",registro["precio"])
    except:
       print("Error en la consulta")



#3. Inserta un nuevo anime.

def Insertar_BD(db,anime):
    cursor = db.cursor()
    sql="insert into Anime values ('"+anime["titulo"]+"', '"+anime["isbn"]+"' ,'"+anime["estudio"]+"' ,'"+anime["genero"]+"' ,'"+anime["fecha"]+"' ,'"+anime["precio"]+"')"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar.")
        db.rollback()

#4. Elimina los animes de un estudio.

def Borrar_BD(db,estudio):
    sql="delete from Anime where estudio= '"+estudio+"'"
    cursor = db.cursor()
    resp=input("¿Realmente quieres borrar el estudio %s? (pulsa 's' para si)" % estudio)
    if resp=="s":
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount==0:
                print("No hay animes de ese estudio")
        except:
            print("Error al borrar.")
            db.rollback()

#5. Empiezan las rebajas, pide un genero por teclado y rebaja los animes que sean de ese genero un 10%.

def Rebajas(db,genero):
    sql= "update Anime set precio= precio-(precio*0.1) where genero= '"+genero+"'"
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existe animes para rebajar.")
        else:
            print ("Precio actualizada correctamente.")
    except:
        print ("Error en la consulta.")

#0. Desconectar 
def Desconectar_BD(db):
    db.close()
