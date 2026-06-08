const readline = require('readline');
// console.log(readline);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout  
});

rl.question('이름을 입력하세요:\n', function (ans) {
    // ans 짝수...ans 를 2 로 나누었을떄 나머지가 0 이면 짝수, 아니면 홀수
    if(ans % 2 == 0) {
        console.log('짝수입니다');
    } else {
        console.log('홀수입니다');
    }
    rl.close();
})