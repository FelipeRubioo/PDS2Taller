import pyodbc
from Conecction import connection, cursor

class Cliente:
    def __init__(self,nombreCliente: str, rfc: str,email: str, telefono:str , direccion: str ) -> None:
        self.nombreCliente = nombreCliente
        self.rfc = rfc
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def registrarCliente(nombreCliente: str, rfc: str,email: str, telefono:str , direccion: str ):
        cliente = Cliente(nombreCliente, rfc, email, telefono, direccion)
        
        #se agrega a la base de datos

        sqlQuery = "INSERT INTO Cliente (nombreCliente, rfc, email, telefono, direccion) VALUES (?,?,?,?,?);"
        cursor.execute(sqlQuery, (str(cliente.nombreCliente), str(cliente.rfc) , str(cliente.email) , str(cliente.telefono) , str(cliente.direccion)))
        connection.commit()
    
    def obtenerClientes(idCliente = "",nombreCliente = "",rfc = "",email = "",telefono = "",direccion = "") -> list:
        with open('FiltroConsultarClientes.sql', 'r') as file:
            sqlQuery = file.read()

        if len(idCliente) == 0:
            idCliente = "NULL"

        if len(nombreCliente) == 0:
            nombreCliente = "NULL"
        else:
            nombreCliente = "'" + nombreCliente + "'"

        if len(rfc) == 0:
            rfc = "NULL"
        else:
            rfc = "'" + rfc + "'"

        if len(email) == 0:
            email = "NULL"
        else:
            email = "'" + email + "'"

        if len(telefono) == 0:
            telefono = "NULL"
        else:
            telefono = "'" + telefono + "'"

        if len(direccion) == 0:
            direccion = "NULL"
        else:
            direccion = "'" + direccion + "'"

        
        cursor.execute(sqlQuery.format(idCliente, nombreCliente, rfc, email, telefono, direccion))
        resultado = cursor.fetchall()
    
        clientes = []
        for cliente in resultado:
            clientes.append(list(cliente))

        return clientes

    
    def actualizarCliente(idCliente,nombreCliente,rfc,email,telefono,direccion) -> None:
        with open('ActualizarCliente.sql','r') as file:
            sqlQuery = file.read()

        cursor.execute(sqlQuery.format(idCliente,nombreCliente,rfc,email,telefono,direccion))
        connection.commit()
        
        

#Cliente.registrarCliente("Felipe Rubio", "RUFI89", "FELIPE9201@GMAIL.COM", "6623251442", "GENERAL PIÑA 66")
