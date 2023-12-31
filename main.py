from flask import Flask,flash, jsonify, render_template,request,redirect,session
from Conecction import cursor
from Cliente import Cliente
from Vehiculo import Vehiculo
from Servicio import Servicio
from Nota import Nota


#app de flask
app = Flask(__name__)
app.secret_key = "asdfvfñfes7u2nairfn"


#Inicio
@app.route("/", methods=['GET','POST'])
def index():
        return redirect("/Login")


#Login 
@app.route("/Login", methods= ["GET","POST"])
def Login():
    if request.method == 'GET':
        return render_template('Login.html')
    
    elif request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña'] 
        #verifica que el usuario existe y la contraseña es correcta
        cursor.execute("SELECT correo FROM Admin where correo = '"+ correo +"' AND contraseña = '"+contraseña+"'")
        resultado = cursor.fetchall()
        filas = len(resultado)

        #el query dio un resultado, el usario existe
        if filas == 1:
            session['logged'] = True
            cursor.execute("SELECT idAdmin FROM Admin where correo = '"+ correo +"'")
            resultado = cursor.fetchall()
            session['idAdmin'] = resultado[0][0]
            session['vehiculos'] = []
            session['clientes'] = []
            session['servicios'] = []
            session['notas'] = []
            print("sesion iniciada correctamente")
            return redirect("/Home")
        #el query no dio match, el usuario no existe
        else:
            print("no se encontro el usuario")
            session['logged'] = False
            return redirect("/Error")

#Pagina Principal 
@app.route("/Home", methods= ["GET","POST"])
def HomeCliente():
    metodo = request.method
    if metodo == 'GET':
            if session['logged'] == True:
                return render_template('Home.html')
                
            else:
                return redirect("/Error")
            
#RegistrarCliente 
@app.route("/RegistrarCliente", methods= ["GET","POST"])
def RegistrarCliente():
        if request.method == 'GET':
             return render_template('RegistrarCliente.html')
    
        elif request.method == 'POST':
            Cliente.registrarCliente(request.form['nombreCliente'], request.form['rfc'], request.form['email'], request.form['telefono'],request.form['direccion'])
            


#ConsultarCliente 
@app.route("/ConsultarCliente", methods= ["GET","POST"])
def ConsultarCliente():
        if session['logged'] == True:

            if request.method == 'GET':
                clientes = session['clientes']
                return render_template('ConsultarCliente.html', listaClientes = clientes)
            
            elif request.method == 'POST':
                 idCliente = request.form['idCliente']
                 nombreCliente = request.form['nombreCliente']
                 rfc = request.form['rfc']
                 email = request.form['email']
                 telefono = request.form['telefono']
                 direccion = request.form['direccion']
                 
                 clientes = Cliente.obtenerClientes(idCliente, nombreCliente, rfc, email, telefono, direccion)
                 session['clientes'] = clientes
                 return redirect("/ConsultarCliente")
        else:
             return render_template('Error.html')

#EditarCliente
@app.route("/EditarCliente", methods = ["GET","POST"])
def EditarCliente():
        if session['logged'] == True:
              if request.method =='GET':
                   return render_template("EditarCliente.html")
              
              if request.method == 'POST':
                  idCliente = request.form['idCliente']
                  nombreCliente = request.form['nombreCliente']
                  rfc = request.form['rfc']
                  email = request.form['email']
                  telefono = request.form['telefono']
                  direccion = request.form['direccion']
                  
                  Cliente.actualizarCliente(idCliente,nombreCliente,rfc,email,telefono,direccion)
                   
                  return "se actualizo el cliente"
              

#RegistrarVehiculo
@app.route("/RegistrarVehiculo", methods= ["GET","POST"])
def RegistrarVehiculo():
        if request.method == 'GET':
            return render_template('RegistrarVehiculo.html')
        
        elif request.method == 'POST':
            Vehiculo.registrarVehiculo(request.form['marca'], request.form['modelo'], request.form['color'], request.form['kilometraje'], request.form['numeroSerie'], request.form['placa'], request.form['idCliente'])

#ConsultarVehiculo 
@app.route("/ConsultarVehiculo", methods= ["GET","POST"])
def ConsultarVehiculo():
        if session['logged'] == True:
            if request.method == 'GET':
           
             vehiculos = session['vehiculos'] 
             return render_template('ConsultarVehiculo.html', listaVehiculos = vehiculos)
            
            elif request.method == 'POST':
                 idVehiculo = request.form['IDVehiculo']
                 marca = request.form['Marca']
                 modelo = request.form['Modelo']
                 color = request.form['Color']
                 kilometraje = request.form['Kilometraje']
                 nSerie = request.form['NumeroSerie']
                 placa = request.form['Placa']
                 idCliente = request.form['IDCliente']
                
                
                 vehiculos = Vehiculo.obtenerVehiculos(idCliente, idVehiculo,marca,modelo,color,kilometraje,nSerie, placa)
                 session['vehiculos'] = vehiculos
                 return redirect("/ConsultarVehiculo")
                 
        else:
             return render_template('Error.html')
        
@app.route("/EditarVehiculo", methods = ["GET","POST"])
def EditarVehiculo():
        if session['logged'] == True:
              if request.method =='GET':
                   return render_template("EditarVehiculo.html")
              
              if request.method == 'POST':
                  idVehiculo = request.form['idVehiculo']
                  marca = request.form['marca']
                  modelo = request.form['modelo']
                  color = request.form['color']
                  kilometraje = request.form['kilometraje']
                  nSerie = request.form['nSerie']
                  placa = request.form['placa']
                  idCliente = request.form['idCliente']
                  
                  Vehiculo.actualizarVehiculo(idVehiculo,marca,modelo,color,kilometraje,nSerie, placa,idCliente)
                   
                  return "se actualizo el vehiculo"
                   
                  
@app.route("/PaginaEditarVehiculo", methods = ["GET","POST"])
def paginaEditarVehiculo():
     if session['logged'] == True:
          if request.method == 'GET':
               return render_template("EditarVehiculo.html")

#RegistrarServicio
@app.route("/RegistrarServicio", methods= ["GET","POST"])
def RegistrarServicio():
     if session['logged'] == True:
         if request.method == 'GET':
             return render_template('RegistrarServicio.html')
         
         elif request.method == 'POST':
            producto = request.form.get('producto')
            if producto is not None:
                producto = 1
            else:
                producto = 0
            Servicio.registrarServicio(request.form['nombreServicio'], request.form['precio'], producto)
          

#ConsultarServicio 
@app.route("/ConsultarServicio", methods= ["GET","POST"])
def ConsultarServicio():
        if session['logged'] == True:
            if request.method == 'GET':
        
             servicios = session['servicios'] 
             return render_template('ConsultarServicio.html', listaServicios = servicios)
            
            elif request.method == 'POST':
                 idServicio = request.form['idServicio']
                 nombreServicio = request.form['nombreServicio']
                 precio = request.form['precio']
    
                 producto = request.form.get('producto')
                 
                 if producto is not None:
                      producto = "checked"
                 else:
                      producto = ""

                 servicios = Servicio.obtenerServicios(idServicio,nombreServicio,precio,producto)
                 session['servicios'] = servicios
                 return redirect("/ConsultarServicio")
        else:
             return render_template('Error.html')
        
#EditarServicio
@app.route("/EditarServicio", methods = ["GET","POST"])
def EditarServicio():
        if session['logged'] == True:
              if request.method =='GET':
                   return render_template("EditarServicio.html")
              
              if request.method == 'POST':
                  idServicio = request.form['idServicio']
                  nombreServicio = request.form['nombreServicio']
                  precio = request.form['precio']
                  producto = request.form.get('producto')
                  if producto is not None:
                      producto = request.form['producto']
                  else:
                      producto = ""
                  Servicio.actualizarServicio(idServicio,nombreServicio,precio,producto)
                  
                  return "se actualizo el servicio"
              
#RegistrarNota
@app.route("/RegistrarNota", methods= ["GET","POST"])
def RegistrarNota():
        if session['logged'] == True:
            if request.method == 'GET':
                
                clientes = Cliente.obtenerClientes()
                servicios = Servicio.obtenerServicios()
                return render_template('RegistrarNota.html', listaClientes = clientes, listaServicios = servicios)
        
        if request.method == 'POST':
             idCliente = request.form['nombreCliente']
             idVehiculo = request.form['vehiculo']
             idServicio = request.form['servicio']
             cantidad = request.form['cantidad']
             fechaPlazo = request.form['fechaPlazo']
             facturado = request.form.get('facturado')
             if facturado is not None:
                 facturado = 1
             else:
                 facturado = 0
             precioNeto = request.form['precioNeto']
             precioImpuestos = request.form['precioImpuestos']
             precioTotal = request.form['precioTotal']
             print("datos: " + idCliente, idVehiculo, idServicio, cantidad, fechaPlazo , facturado , precioNeto, precioImpuestos, precioTotal)
             Nota.registrarNota(idCliente, idVehiculo, idServicio, cantidad, fechaPlazo , facturado , precioNeto, precioImpuestos, precioTotal)
        else:
            return render_template('Error.html')


#ConsultarNota
@app.route("/ConsultarNota", methods= ["GET","POST"])
def ConsultarNota():
        if session['logged'] == True:
            if request.method == 'GET':
                
             notas = session['notas']
             return render_template('ConsultarNota.html', listaNotas = notas)
            
            elif request.method == 'POST':
                 idNota = request.form['idNota']
                 fechaGeneracion = request.form['fechaGeneracion']
                 plazoCredito = request.form['plazoCredito']
                 facturado = request.form.get('facturado')
                 if facturado is not None:
                      facturado = request.form['facturado']
                 else:
                      facturado = ""
                 idCliente = request.form['idCliente']
                 idVehiculo = request.form['idVehiculo']
                 idServicio = request.form['idServicio']
                 cantidad = request.form['cantidad']
                 precioNeto = request.form['precioNeto']
                 precioImpuestos = request.form['precioImpuestos']
                 precioTotal = request.form['precioTotal']
                 notas = Nota.obtenerNotas(idNota, fechaGeneracion, plazoCredito,facturado,idCliente,idVehiculo,idServicio,
                     cantidad,precioNeto,precioImpuestos,precioTotal)
                 
                 session['notas'] = notas
                 return redirect("/ConsultarNota")
        else:
             return render_template('Error.html')


#SelectVehiculos        
@app.route("/SelectVehiculos", methods= ["POST"])
def selectVehiculos():
     if request.method == 'POST':
    
            data = request.get_json()
            idCliente = data.get('idCliente')

            
            # Your logic to process the number and generate an array
            
            listaVehiculos = Vehiculo.obtenerVehiculos(idCliente)
            return jsonify(listaVehiculos)
     
if __name__ == "__main__":
    app.run(debug=True)