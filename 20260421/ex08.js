const { reverse } = require("node:dns/promises");

function solution(numbers) {
    var answer = 0;
    for (i = 0; i < numbers.length; i++) {
        answer = answer + numbers[i];
        console.log(numbers[i]);
        console.log('answer '+answer)
    }
        number = answer / numbers.length
            console.log('number '+number)

    return number;
}
result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
console.log(result)

function solution(array, height) {
    var answer = 0;
    for (let i = 0; i < array.length; i++){
        if (array[i] > height){
            answer = answer + 1
        }
    }
    return answer;
}
result = solution([149, 180, 192, 170], 167)
console.log(result)

function solution(money) {
    var answer = [];
    const a = money % 5500;
    const b = money / 5500;
    var c = parseInt(b);

    answer.unshift(c)
    answer.push(a) 
    return answer;
}
result = solution(15000);
console.log(result);

function solution(num_list) {
    var answer = [];    
    for(let i=num_list.length-1; i >= 0; i--) {
        answer.push(num_list[i]);
    }
    return answer;
}   
result = solution([1, 2, 3, 4, 5]);
console.log(result)

function solution(my_string) {
    var answer = '';  
    for(let i=my_string.length-1; i >= 0; i--) {
        answer = answer + my_string[i]
    }  
    return answer;
}
result = solution("bread");
console.log(result)

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