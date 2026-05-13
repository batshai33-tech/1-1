function solution(numbers, num1, num2) {
    var answer = [];
    answer = numbers.slice(num1, num2+1)
    return answer;
}
result = solution([1, 2, 3, 4, 5],1 ,3)
console.log(result)


function solution(start_num, end_num) {
    var answer = [];
    for(let i = start_num ; i <= end_num ;i++){
        answer.push(i)
    }
    return answer;
}
result = solution(3, 10)
console.log(result)


