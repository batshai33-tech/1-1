console.log(!true)
console.log(!false) 

if(!false && 10 < 20 || false){
    console.log('출력');
}

const tt = '';
if(tt) { console.log(' tt true'); }

const test = {}
if(test){
    console.log('test true');
}

// !는 그 값을 부정한다는 뜻이다 !true 는 false 가 된다
// 괄호안의 모든수는 0 null 을 재외한 모든수는 트루가 된다
// 만약 아무것도 없으면 ''는 거짓 {}는 참 이된다

// string -> number
const num = Number('10')

