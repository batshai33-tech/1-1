function solution(n, k) {
    var answer = 0;
    var survise = Math.floor(n / 10)
    answer = ((n * 12000) + (k * 2000))
    answer = answer - (survise * 2000)
    return answer
}
result = solution(64,6)
console.log(result)