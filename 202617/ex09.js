var a = 10>20;
var b = 30<40;

console.log(a && b); // 둘다
console.log(a || b); // 둘중 하나만
console.log(!a); // 부정문 본례 값의 반대(ture 가 출력되야하면 false 로)

var a = 10;
var f = false && ++a;
console.log(f);
console.log(a);

