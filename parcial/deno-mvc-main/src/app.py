from flask import Flask,jsonify,request,make_response
from controllers.usuario import UserControl


userControl = UserControl()
app = Flask (__name__)
  


@app.route('/listado', methods = ['GET'])

def listando():
   
    lista = userControl.listado()
    return make_response(jsonify(lista), 200)

@app.route('/crear', methods = ['POST'])

def creando():

    nombre = request.json ["nombre"]
    apellido = request.json ["apellido"]
    celular = request.json ["celular"]
    correo = request.json ["correo"]
    contrasenia = request.json ["contrasenia"]

    creacion = userControl.crear(nombre,apellido,celular,correo,contrasenia)

@app.route('/actualizar/<cod>', methods = ['PUT'])

def actualizando(cod):

    nombre = request.json ["nombre"]
    apellido = request.json ["apellido"]
    celular = request.json ["celular"]
    correo = request.json ["correo"]
    contrasenia = request.json ["contrasenia"]

    creacion = userControl.actualizar(nombre,apellido,celular,correo,contrasenia,cod)

@app.route('/eliminar/<cod>', methods = ['DELETE'])

def borrando(cod):
    userControl.borrar(cod)

@app.route('/listarbd', methods = ['GET'])

def listarbd():
    databases = userControl.listarbd()
    return make_response(jsonify(databases), 200)


@app.route('/creardatabase', methods = ['POST'])
def creardatabase():

    name = request.json ["name"]
    creaciondb = userControl.creardatabase(name)
    return 'Base de datos Creada'

@app.route('/mostrartablas/<nombretabla>', methods = ['GET'])
def mostrartablas(nombretabla):

    mostrartablas = userControl.mostrartablas(nombretabla)
    return make_response(jsonify(mostrartablas), 200)

@app.route('/describirtabla', methods = ['GET'])
def describirtablas():

    mostrartablas = userControl.describirprueba()
    return make_response(jsonify(mostrartablas), 200)

@app.route('/editartabla/<nombretabla>/<nombrecolumna>', methods = ['PUT'])
def editartabla(nombretabla,nombrecolumna):

    descripcion = request.json ["descripcion"]
    tipodato = request.json ["tipodato"]
    alteracion = userControl.editartabla(nombretabla,nombrecolumna,descripcion,tipodato)
    return 'Cambio realizado con exito'
    
app.run(debug=True)  