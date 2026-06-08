function solution(st,en){
    console.log(`st = ${st} en = ${en}`)
    const answer = [];

    for(let i = st; i <= en; i++){
        console.log(`i = %{i}`)
    answer.push(i); 
    // 배열함수인 push pop slice 함수사용가능
    }
    return answer;

}

const result = solution(3,5);
console.log(result);
 