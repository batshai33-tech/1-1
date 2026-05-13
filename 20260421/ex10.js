function solution(my_string, letter) {
    var answer = '';
    for(let i = 0; i < my_string.length;i++){
        if(my_string[i] != letter)
            answer += my_string[i]
    }
    return answer;
}
result = solution("abcdef", "c")
console.log(result)

function solution(angle) {
    var answer = 0;
    if(0 < angle && angle < 90){
        answer += 1;
    } else if(angle == 90){
        answer += 2;
    } else if(90 < angle && angle < 180){
        answer += 3;
    } else if(angle == 180){
        answer += 4;
    }
    return answer;
}
result = solution(100);
console.log(result);