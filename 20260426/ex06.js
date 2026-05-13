//...

const arr1 = ['a','b','c','d'];
const arr2 = ['e','f','g','h'];

console.log([...arr1 , ...arr2]);

const ss = new Set();

ss.add('a');
ss.add('a');
ss.add('a');
ss.add('b');
ss.add('b');
ss.add('c');
ss.add('c');
console.log(ss);
console.log([...ss]);
console.log(ss.size);

const ss1 = new Set('We are the world');
console.log(ss1);
console.log([...ss1])
console.log([...ss1].join(''))