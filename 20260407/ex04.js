function solution(arr, delete_list) {
    var answer = [];
    for (let i = 0; i < arr.length; i++) {
        let v1 = arr[i];
        if (!delete_list.includes(v1)) {
            answer.push(v1);
        }
    }
    return answer;
}