import pyodbc
from Conecction import connection, cursor

class Servicio:
    def __init__(self,nombreServicio: str, precio: float , producto: bool = False) -> None:
        self.nombreServicio = nombreServicio
        self.precio = precio
        self.producto = producto

    def registrarServicio(nombreServicio: str, precio: float , producto:bool):
        servicio = Servicio(nombreServicio,precio,producto)
        
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Servicio (nombreServicio, precio , producto) VALUES (?,?,?);"
        cursor.execute(sqlQuery, (str(servicio.nombreServicio), float(servicio.precio) , int(servicio.producto)))
        connection.commit()

    def obtenerServicios(idServicio = "",nombreServicio = "",precio = "",producto = "") -> list:
        with open('FiltroConsultarServicios.sql', 'r') as file:
            sqlQuery = file.read()

        if len(idServicio) == 0:
            idServicio = "NULL"

        if len(nombreServicio) == 0:
            nombreServicio = "NULL"
        else:
            nombreServicio = "'" + nombreServicio + "'"

        if len(precio) == 0:
            precio = "NULL"
        else:
            precio = "'" + precio + "'"

        if len(producto) == 0:
            producto = "NULL"
        else:
            producto = 1

        cursor.execute(sqlQuery.format(idServicio, nombreServicio, precio, producto))
        resultado = cursor.fetchall()
    
        servicios = []
        for servicio in resultado:
            servicios.append(list(servicio))

        return servicios
    
    
    def actualizarServicio(idServicio,nombreServicio,precio,producto) -> None:
        with open('ActualizarServicio.sql','r') as file:
            sqlQuery = file.read()

        if len(producto) == 0:
            producto = 0
        else:
            producto = 1
            
        cursor.execute(sqlQuery.format(idServicio,nombreServicio,precio,producto))
        connection.commit()
#Servicio.registrarServicio("cambio de aceite", 200.30)
