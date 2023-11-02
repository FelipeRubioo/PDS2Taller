import pyodbc

#Inicio conexion a base de datos 
try:
    #aqui, cambien aurora por el nombre de su server, database por el nombre de la base de datos, UID Y PWD son el usuario y contraseña para conectarse con credenciales de sql server
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=AURORA;DATABASE=ProyectoTaller;UID=Felipe;PWD=rubio')
    print("conexion exitosa")
    cursor = connection.cursor()

except Exception as ex:
    print (ex)
#Fin conexion a base de datos 