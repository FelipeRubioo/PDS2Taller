import pyodbc

class Servicio:
    def __init__(self,nombreServicio: str, precio: float , producto: bool = False) -> None:
        self.nombreServicio = nombreServicio
        self.precio = precio
        self.producto = producto

    def registrarServicio(nombreServicio: str, precio: float , producto:bool):
        from main import cursor, connection
        servicio = Servicio(nombreServicio,precio,producto)
        
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Servicio (nombreServicio, precio , producto) VALUES (?,?,?);"
        cursor.execute(sqlQuery, (str(servicio.nombreServicio), float(servicio.precio) , int(servicio.producto)))
        connection.commit()

#Servicio.registrarServicio("cambio de aceite", 200.30)
