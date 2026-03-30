let num = 1;
let sum = 0;
// while(조건){}
// for(초기값; 조건; 증감식){}

while(num != 11){
    console.log(num);
    sum += num;
    console.log(`sum = ${sum}`);
    num++;
}
console.log(`sum = ${sum}`);