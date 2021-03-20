import { oak } from '../moduls.ts'
import {UsuarioController} from '../controllers/usuario1.ts'

const usuarioController =new UsuarioController();
const {Router} = oak
const router = new Router()

router
    .get('/usuarios', usuarioController.listar)
    .post('/usuarios', usuarioController.create)
    .delete('/usuarios/:id', usuarioController.eliminar)
    .put('/usuarios/:id', usuarioController.actualizar)
export default router