from config.mariadb import DB

import mariadb

class UsuariosModel():
    
    def listar(self):

        cursor = DB.cursor()
        cursor.execute('select * from datosuser ')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    def crear(self, nombre, apellido, celular, correo, contrasenia):
        
        cursor = DB.cursor()
        cursor.execute('insert into datosuser(nombre,apellido,celular,correo,contrasenia) values(?,?,?,?,?)', 
        (nombre,apellido,celular,correo,contrasenia,))
        cursor.close()

     
    def eliminar(self, cod):

        cursor = DB.cursor()
        cursor.execute('delete from datosuser WHERE id = ? ', cod)
        cursor.close()

        
    def actualizar(self,nombre,apellido,celular,correo,contrasenia,cod):

        cursor = DB.cursor()
        cursor.execute('update datosuser set nombre = ?, apellido = ?, celular = ?, correo = ?, contrasenia = ? WHERE id = ? ', 
        (nombre,apellido,celular,correo,contrasenia,cod))
        cursor.close()

    def mostrardatabase (self):

        cursor = DB.cursor()
        cursor.execute('SHOW DATABASES')
        databases = cursor.fetchall()
        cursor.close()
        return databases

    def creardatabase (self, name):

        cursor = DB.cursor()
        cursor.execute('CREATE DATABASE '+ name)
        cursor.close()


    def describirprueba (self):
        
        cursor = DB.cursor()
        cursor.execute('SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = "user"')
        ssql = cursor.fetchall()
        print (ssql)
        lista=[]
        for x in ssql:
            for z in x:
                print(z)
                cursor.execute('DESC '+ z)
                ssql2 = cursor.fetchall() 
                print(ssql2)
                lista.append(ssql2)
        cursor.close()
        return lista

    def describirtablas (self,name):

        cursor = DB.cursor()
        cursor.execute('DESCRIBE '+name)
        descripciones= cursor.fetchall()
        cursor.close()
        return descripciones

    def creartabla (self,nombre_tabla, nombrecolumna):

        cursor = DB.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS '+ nombre_tabla + ' '+nombre_tabla+',' +nombrecolumna+',VARCHAR(30);')
        mistablas = cursor.fetchall()
        cursor.close()
        return mistablas

    def alterartabla (self,nombretabla,nombrecolumna,descripcion,tipodato):

        cursor = DB.cursor()
        cursor.execute('ALTER TABLE '+nombretabla+' CHANGE '+nombrecolumna+' '+descripcion+' '+tipodato+';')
        cursor.close()
        


    
