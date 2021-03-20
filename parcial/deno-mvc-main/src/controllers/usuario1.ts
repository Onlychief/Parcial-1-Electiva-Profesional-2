import {UsuariosModel} from '../models/user1.ts'
import {UsuarioDTO} from '../dto/usuarios.ts'
import { dataUser } from "../DataUtils.ts";
import {Context} from 'https://deno.land/x/oak/mod.ts'


const usuariosModel =  new UsuariosModel()

export class UsuarioController{

async listar(context:Context){
    const usuarios = await usuariosModel.listar();
    context.response.body =usuarios
}
async create(context:Context){
    const usuario = await(context.request.body().value)
    await usuariosModel.crear(usuario)
    context.response.body = {
        message: 'Usuario Creado Correctamente'
    }
}
async actualizar(context:any){
    const usuario = await(context.request.body().value)
    await usuariosModel.actualizar(usuario,context.params.id)
    context.response.body = {
        message: 'Usuario Actualizado Correctamente'
}
}
async eliminar(context: any) {
    await usuariosModel.deletear(context.params.id)
    await (context.response.body = 'Eliminando ando') 
}
}