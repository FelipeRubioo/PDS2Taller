import pyodbc
from Conecction import connection, cursor

class Vehiculo:
    def __init__(self,marca: str, modelo: str,color: str, kilometraje:str , numeroSerie: str ,placa: str, idCliente: int ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = kilometraje
        self.numeroSerie = numeroSerie
        self.placa = placa
        self.idCliente = idCliente

    def registrarVehiculo(marca: str, modelo: str,color: str, kilometraje:str , numeroSerie: str ,placa: str, idCliente: int):
        vehiculo = Vehiculo(marca,modelo,color, kilometraje,numeroSerie,placa,idCliente)
        
        #se agrega a la base de datos
        sqlQuery = "INSERT INTO Vehiculo (marca, modelo, color, kilometraje, numeroSerie, placa , idCliente) VALUES (?,?,?,?,?,?,?);"
        cursor.execute(sqlQuery, (str(vehiculo.marca), str(vehiculo.modelo) , str(vehiculo.color) , str(vehiculo.kilometraje) , str(vehiculo.numeroSerie), str(vehiculo.placa),  int(vehiculo.idCliente) ))
        connection.commit()




    def obtenerVehiculos(idVehiculo,marca,modelo,color,kilometraje,nSerie,placa, idCliente) -> list:
        with open('FiltroConsultarVehiculos.sql', 'r') as file:
            sqlQuery = file.read()

        if len(idVehiculo) == 0:
            idVehiculo = "NULL"

        if len(marca) == 0:
            marca = "NULL"
        else:
            marca = "'" + marca + "'"

        if len(modelo) == 0:
            modelo = "NULL"
        else:
            modelo = "'" + modelo + "'"

        if len(color) == 0:
            color = "NULL"
        else:
            color = "'" + color + "'"

        if len(kilometraje) == 0:
            kilometraje = "NULL"
        else:
            kilometraje = "'" + kilometraje + "'"

        if len(nSerie) == 0:
            nSerie = "NULL"
        else:
            nSerie = "'" + nSerie + "'"

        if len(placa) == 0:
            placa = "NULL"
        else:
            placa = "'" + placa + "'"
        
        if len(idCliente) == 0:
            idCliente = "NULL"

        cursor.execute(sqlQuery.format(idVehiculo, marca, modelo, color, kilometraje, nSerie, placa, idCliente))
        resultado = cursor.fetchall()
    
        vehiculos = []
        for vehiculo in resultado:
            vehiculos.append(list(vehiculo))

        return vehiculos

    def actualizarVehiculo(idVehiculo,marca,modelo,color,kilometraje,nSerie,placa,idCliente) -> None:
        with open('ActualizarVehiculos.sql', 'r') as file:
            sqlQuery = file.read()

        cursor.execute(sqlQuery.format(idVehiculo, marca, modelo, color, kilometraje, nSerie, placa, idCliente))
        connection.commit()


#Vehiculo.registrarVehiculo("volkswagen","bocho","gris","14265","1458712","wer14552",2)