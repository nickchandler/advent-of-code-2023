import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const data = fs.readFileSync(`${__dirname}/input.txt`);

const dataParsed = Buffer.from(data).toString();

const dataArr = dataParsed.split('\n');

/*
input: string[]
output: number
*/
function solution(input) {
  let sum = 0;

  for (let code of input) {
    if (!code.length) continue;
    console.log(`analyzing "${code}"...`);

    let codeNum;
    let dig1;
    let dig2;
    let forwardIndex = 0;
    let backwardIndex = code.length - 1;
    while (codeNum === undefined) {
      if (dig1 === undefined) {
        if (Number.isInteger(parseInt(code[forwardIndex]))) {
          dig1 = code[forwardIndex];
          continue
        } else {
          forwardIndex++;
          continue;
        }
      }

      if (Number.isInteger(parseInt(code[backwardIndex]))) {
        dig2 = code[backwardIndex];
      } else {
        backwardIndex--;
        continue;
      }

      codeNum = dig1 + dig2;
      console.log(`...${parseInt(dig1 + dig2)}!`)
    }
    sum += parseInt(codeNum);
  }
  return sum;
}

console.log(solution(dataArr));
