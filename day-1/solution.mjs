import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const data = fs.readFileSync(`${__dirname}/input.txt`);

const dataParsed = Buffer.from(data).toString();

const dataArr = dataParsed.split('\n');

const wordDigitMap = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

// This is some ugly ass code and the time complexity can certainly be improved. It works though.
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

    let currWord = '';
    while (codeNum === undefined) {
      console.log(currWord);
      if (dig1 === undefined) {
        if (Number.isInteger(parseInt(code[forwardIndex]))) {
          dig1 = code[forwardIndex];
          currWord = '';
          continue
        } else {
          currWord = currWord + code[forwardIndex];
          if (wordDigitMap[currWord]) {
            dig1 = wordDigitMap[currWord];
            currWord = '';
            continue;
          }

          for (let i = 0; i < currWord.length; i++) {
            const substrBack = currWord.slice(-i);
            const substrForw = currWord.slice(0, i + 1);
            if (wordDigitMap[substrBack]) {
              dig1 = wordDigitMap[substrBack];
              currWord = '';
              continue;
            }
            if (wordDigitMap[substrForw]) {
              dig1 = wordDigitMap[substrForw];
              currWord = '';
              continue;
            }
          }

          forwardIndex++;
          continue;
        }
      }

      if (Number.isInteger(parseInt(code[backwardIndex]))) {
        dig2 = code[backwardIndex];
        currWord = '';
      } else {
        currWord = code[backwardIndex] + currWord;
        if (wordDigitMap[currWord]) {
          dig2 = wordDigitMap[currWord];
          currWord = '';
        } else {
          for (let i = 0; i < currWord.length; i++) {
            const substrBack = currWord.slice(-i);
            const substrForw = currWord.slice(0, i + 1);
            if (wordDigitMap[substrBack]) {
              dig2 = wordDigitMap[substr];
              currWord = '';
              break;
            }
            if (wordDigitMap[substrForw]) {
              dig2 = wordDigitMap[substrForw];
              currWord = '';
              break;
            }
          }
          if (dig2 === undefined) {
            backwardIndex--;
            continue;
          }
        }
      }

      codeNum = dig1 + dig2;
      console.log(`...${parseInt(dig1 + dig2)}!`)
    }
    sum += parseInt(codeNum);
  }
  return sum;
}

console.log(solution(dataArr));
