import mysql.connector
conexion=mysql.connector.connect(
    user='root',
    password='123456789',
    host='localhost',
    database='registros',
    port='3306'
                                 )
print(conexion)
cursor=conexion.cursor()