const arr = [1, 2, 3, 4, 5, 6,]
// 1 ~ 3 까지 잘라라 새로 만들어라
const result = arr.slice(1,3);
console.log(`result = ${result}`);
console.log(`arr = ${arr}`);
// 1 ~ 3 까지 삭제해라
arr.splice(1,3);
console.log(`arr = ${arr}`);

console.log([1, 2, 3].concat([4, 5, 6]));
console.log([1, 2, 3] + [4, 5, 6]);