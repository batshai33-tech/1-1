const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('다이쓰! 무조건 천원, 상품입력?', function (obj) {
    let dic = {
        [obj]: "친구"
    }
    console.log(dic);
    console.log(dic[obj]);
    rl.close();
});