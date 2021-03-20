from models.user import UsuariosModel
from flask import Flask, jsonify, request

class UserControl():

    def listado(self):

        usuarioslis =UsuariosModel()
        usuarios = usuarioslis.listar()
        return (usuarios)  
   
    def crear(self, nombre, apellido, celular, correo, contrasenia):
 
        usuariocrear =UsuariosModel()
        usuariocrear.crear(nombre,apellido,celular,correo,contrasenia)
    
    def actualizar(self, nombre, apellido, celular, correo, contrasenia,cod):
 
        usuarioactualizar =UsuariosModel()
        usuarioactualizar.actualizar(nombre,apellido,celular,correo,contrasenia,cod)

    def borrar(self, cod):
     
        usuarioborrar =UsuariosModel()
        usuarioborrar.eliminar(cod)


    def listarbd(self):

        user = UsuariosModel()
        databases = user.mostrardatabase()
        return (databases)

    def creardatabase(self, name):

        name = request.json['name']
        user = UsuariosModel()
        user.creardatabase(name)
        return 'hecho'

    def mostrartablas(self):

        user = UsuariosModel()
        mostrartablas = user.mostrartablas()
        return (mostrartablas)
    
    def editartabla(self,nombretabla, nombrecolumna, descripcion,tipodato):
 
        editartabla =UsuariosModel()
        editartabla.alterartabla(nombretabla, nombrecolumna,descripcion,tipodato)