import pyodbc
from Conecction import connection, cursor

class Nota:
    def __init__(self, idCliente: int , idVehiculo: int, idServicio: int, cantidad:int, fechaPlazo: str ,
                 facturado: int , precioNeto: float , precioImpuestos: float, precioTotal: float) -> None:
        self.idCliente = idCliente
        self.idVehiculo = idVehiculo
        self.idServicio = idServicio
        self.cantidad = cantidad
        self.fechaPlazo = fechaPlazo
        self.facturado = facturado
        self.precioNeto = precioNeto
        self.precioImpuestos = precioImpuestos
        self.precioTotal = precioTotal


    def registrarNota(idCliente: int , idVehiculo: int, idServicio: int, cantidad:int, fechaPlazo: str ,
                 facturado: int , precioNeto: float , precioImpuestos: float, precioTotal: float):
        
        with open('RegistrarNota.sql','r') as file:
            sqlQuery = file.read()

        print(sqlQuery.format(fechaPlazo,facturado,idCliente,idVehiculo,idServicio,cantidad,precioNeto,precioImpuestos,precioTotal))
        cursor.execute(sqlQuery.format(fechaPlazo,facturado,idCliente,idVehiculo,idServicio,cantidad,precioNeto,precioImpuestos,precioTotal))
        connection.commit()
    
    def obtenerNotas(idNota="", fechaGeneracion="", plazoCredito="",facturado="",idCliente="",idVehiculo="",idServicio="",
                     cantidadProducto="",precioNeto="",precioImpuestos="",precioTotal="") -> list:
        
        if len(idNota) == 0:
            idNota = "NULL"
        if len(fechaGeneracion) == 0:
            fechaGeneracion = "NULL"
        else:
            fechaGeneracion = "'" + fechaGeneracion + "'"
        if len(plazoCredito) == 0:
            plazoCredito = "NULL"
        else:
            plazoCredito = "'" + plazoCredito + "'"
        if len(facturado) == 0:
            facturado = "NULL"
        else:
            facturado = 1
        if len(idCliente) == 0:
            idCliente = "NULL"
        if len(idVehiculo) == 0:
            idVehiculo = "NULL"
        if len(idServicio) == 0:
            idServicio = "NULL"
        if len(cantidadProducto) == 0:
            cantidadProducto = "NULL"
        if len(precioNeto) == 0:
            precioNeto = "NULL"
        if len(precioImpuestos) == 0:
            precioImpuestos = "NULL"
        if len(precioTotal) == 0:
            precioTotal = "NULL"
        
        with open('FiltroConsultarNotas.sql', 'r') as file:
            sqlQuery = file.read()

        cursor.execute(sqlQuery.format(idNota, fechaGeneracion, plazoCredito,facturado,idCliente,idVehiculo,idServicio,
                     cantidadProducto,precioNeto,precioImpuestos,precioTotal))
        
        resultado = cursor.fetchall()
    
        notas = []
        for nota in resultado:
            notas.append(list(nota))

        return notas

        
        

    