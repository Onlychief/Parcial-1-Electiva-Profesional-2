import {mysql} from '../moduls.ts'
const {Client} = mysql

export const client = await new Client().connect({
    hostname: 'localhost',
    username: 'root',
    db: 'user',
    password: '',
    port: 3306,
});