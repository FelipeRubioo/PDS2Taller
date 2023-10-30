import pyodbc


class Cliente:
    def __init__(self,nombreCliente: str, rfc: str,email: str, telefono:str , direccion: str ) -> None:
        self.nombreCliente = nombreCliente
        self.rfc = rfc
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def registrarCliente(nombreCliente: str, rfc: str,email: str, telefono:str , direccion: str ):
        from main import cursor, connection
        cliente = Cliente(nombreCliente, rfc, email, telefono, direccion)
        
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Cliente (nombreCliente, rfc, email, telefono, direccion) VALUES (?,?,?,?,?);"
        cursor.execute(sqlQuery, (str(cliente.nombreCliente), str(cliente.rfc) , str(cliente.email) , str(cliente.telefono) , str(cliente.direccion)))
        connection.commit()
    
    def obtenerClientes(idCliente,nombreCliente,rfc,email,telefono,direccion) -> list:
        with open('FiltroConsultarClientes.sql', 'r') as file:
            sqlQuery = file.read()

        if len(idVehiculo) == 0:
            idVehiculo = "NULL"

        if len(marca) == 0:
            marca = "NULL"

        if len(modelo) == 0:
            modelo = "NULL"
        
        if len(color) == 0:
            color = "NULL"
        
        if len(kilometraje) == 0:
            kilometraje = "NULL"
        
        if len(nSerie) == 0:
            nSerie = "NULL"

        if len(placa) == 0:
            placa = "NULL"
        
        if len(idCliente) == 0:
            idCliente = "NULL"

        
        #cursor.execute(sqlQuery.format(idVehiculo, marca, modelo, color, kilometraje, nSerie, placa, idCliente))
        #resultado = cursor.fetchall()
    
       # vehiculos = []
        #for vehiculo in resultado:
         #   vehiculos.append(list(vehiculo))

        #return vehiculos
#Cliente.registrarCliente("Felipe Rubio", "RUFI89", "FELIPE9201@GMAIL.COM", "6623251442", "GENERAL PIÑA 66")
