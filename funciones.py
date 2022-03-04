import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)


def Listar_animes(db):
    sql="SELECT * FROM Animes"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print ("No existen animes en la base de datos.")
        else:    
            animes = cursor.fetchall()
            #print("Tabla de animes")
            for anime in animes:
                print(anime[])
    except:
        print("Error al consultar los datos.")
