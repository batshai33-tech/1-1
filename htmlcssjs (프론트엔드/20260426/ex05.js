const [r, g,...rest] = ['red','green','blue','asdasfa',() => console.log('화살표')];
console.log(r);
console.log(g);

console.log(rest[0]);
console.log(rest[1]);
console.log(rest[2]);
rest[2]();