function aa(){
    let test = 10;
    console.log(test);
}
const vv = ()=>{
    let test2 = 20;
    console.log(test2);
}
// `` 탬플릿 문자열

let num = 0;
for(;num < 100;num = num + 10){
    console.log("Hello World"+num);
    console.log(`Hello World${num}`);
}
console.log(`for 구문이 끝나고 num = ${num}`);
console.log(aa);
aa();
console.log(vv);
vv();
