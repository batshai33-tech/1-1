const arr = [];

arr.push('aa');
arr.push('vv');
console.log(arr);
const result = arr.pop();

console.log(result);
console.log(arr);
//push arr안에다가 aa 와 vv를 넣는다
//pop arr안에 맨뒤에있는 vv를 빼서 출력한다


//배열안에 요소추가 .push 요소 맨뒤를 꺼내며 삭제는 .pop
//for 를 forof 와 foraEach 를 써서 더 간단히 가능 forEach를 많이 씀
//기본자료에 함수를 넣어서 출력할수도있고 추후 오브젝트를 이용해서도 출력이 가능하다