function solution(start_num, end_num) {
    var answer = [];

    let a = start_num;
    while (a <= end_num) {
        answer.push(a);
        a++;
    }
    return answer;
}

const result = solution(3, 5);
console.log(result);

// start_num 에서 end_num까지의 숫자를
// 배열로 출력하세요

// 만약에 3,5 입력하였으면 배열 [3,4,5]반환
// 만약에 1,3 입력하였으면 배열 [1,2,3]반환
