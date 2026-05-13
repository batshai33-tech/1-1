function solution(age) {
    var answer = 0;
    const new_year = 2023 - age
    answer = answer + new_year
    return answer;
}
result = solution(40);
console.log(result);

function solution(num1, num2) {
    var answer = 0;
    const a = num1 / num2
    const b = parseInt(a * 1000);
    answer = answer + b
    return answer;
}

result = solution(7, 3)
console.log(result)

function solution(n) {
    var answer = 0;
    for (i = 1; i <= n; i++){
        if (i % 2 == 0)
            answer = answer + i
    }
    return answer;
}
result = solution(10);
console.log(result)

function solution(n) {
        if (n % 7 == 0){
            return n / 7;
        }else{
            return parseInt(n / 7 + 1)
        }
}
result = solution(1);
console.log(result);

function solution(numbers) {
    var answer = 0;
    for(i = 0; i <= numbers.length ; i++){
        answer += numbers[i]
    var number = 0;
    number = answer/numbers.length
    }
    return answer;
}
result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
console.log(result)