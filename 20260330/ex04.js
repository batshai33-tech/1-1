const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('팩토리얼 구하기\n', (data) =>{
  console.log(data);
  let value = 1;
  for (let num = 1; num <= data; num++) {
    value = value * num;
  }
  console.log(`value = ${value}`);
  rl.close();

});







// 프론트엔드 (도큐먼트)
//백엔드(리퀘어 리드라인,크리에이트 인터페이스)