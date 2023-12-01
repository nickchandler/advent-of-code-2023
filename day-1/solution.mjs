import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const data = fs.readFileSync(`${__dirname}/input.txt`);

console.log(data);

const dataParsed = Buffer.from(data).toString();
console.log(dataParsed);


