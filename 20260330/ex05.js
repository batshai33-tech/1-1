const arr = ['javascript', 'pythun', 'c++', 'node.js']
//forin = 오브젝트 기준 출력
//forof 배열 기준 출력
// arr 에 있는 요소를 하나씩 가져와 item에 넣어 출력시킨다(출력:콘솔로그(아이탬))
for (const item of arr) {
    console.log(item);
}

//forEach 사용
//function(아이탬) = (아이탬) => {} 화살표 써서 줄이기가능
arr.forEach(item =>{
    console.log(item);
})
//이 위는 for 문이지만 좀더 쉬운 for문이다