import { oak } from './moduls.ts'
import UsuariosRouter from './routes/usuarios.ts'
const {Application, Router} = oak


const app = new Application();

const router= new Router();

router.get('/', (context) => {
    context.response.body = "Hola Mundo desde Oak!!!!";
});

app.use(router.routes());
app.use(UsuariosRouter.routes());

console.log('Servidor escuchando');

await app.listen ({
    port:5000,
});


