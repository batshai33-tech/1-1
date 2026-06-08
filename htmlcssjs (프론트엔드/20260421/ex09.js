function solution(num_list) {
    var answer = [];
    var num1 = 0;
    var num2 = 0;
    for(let i = 0; i < num_list.length; i++){
        if (num_list[i] % 2 == 0){
            num1 += 1;
        }else{
            num2 += 1;
        }
    }
    answer.unshift(num1);
    answer.push(num2);
    return answer;;
}
result = solution([1, 2, 3, 4, 5]);
console.log(result)

function solution(my_string, n) {
    var answer = '';
    for (let i = 0; i < my_string.length; i++){
        answer += my_string[i].repeat(n)
    }
    return answer;
}
result = solution("hello", 3);
console.log(result)

function solution(my_string, letter) {
    var answer = '';
    for(let i = 0; i < my_string.length;i++){
        if(my_string[i] != letter)
            answer += my_string[i]
    }
    return answer;
}
result = solution("abcdef", c)
console.log(result)