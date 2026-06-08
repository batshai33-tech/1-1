function solution(arr1, delete_list){
    let answer = [];

    for (let i = 0; i < arr1.length; i++){
        const arritem = arr1[i];
        console.log(arritem)
        let needdelete = false;
        for(let j = 0; j < delete_list.length; j++){
            const delete_item = delete_list[j];
            if (arritem == delete_list){
                needdelete = true;
                break
          
            }
        }   
            if(!needdelete)
        answer.push(arritem)
    }

    return answer;
}

// 


// i = 0 , j = 0~5
// i = 1 , j = 0~5
// i = 2 , j = 0~5
solution([293, 1000, 395, 678, 94],[94, 777, 104, 1000, 1, 12]);
// [293, 395, 678]