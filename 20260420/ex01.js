const a = 0
function solution(num1, num2){  
    if(num1 == num2){
        return 1
    }else{
        return -1
    }
}
const ret = solution(3, 2);
console.log(ret);

function solution(num1, num2) {
    var answer = 0;
    answer += num1 * num2
    return answer;
}
const result = solution(2, 3)
console.log(result)