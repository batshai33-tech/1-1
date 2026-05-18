def solution(n):
    result = 0
    n = str(n)
    n_str_list = list(n)
    n_int_list = list(map(int, n_str_list))
    for i in n_int_list:
        result = result + i
    return result

a = solution(1234)
print(a)

def solution(array):
    answer = max(array)
    index_i = array.index(answer)
    return [answer, index_i]

result = solution([1, 8, 2])
print(result)

def solution(common):

    if common[1] - common[0] == common[2] - common[1]:
        # 다음 인덱싱 번호와 맨처음 인덱싱 번호를 뺀것과
        # 다른 순서에 있는 인덱싱 번호와 맨처음 인덱싱 번호를 뺀것이 같다면
        # 이는 배수로 증가하는것이 아닌 더하기로 증가하는 값이기에
        return common[-1] + (common[1] - common[0])
        # 마지막 인덱싱 값에다가 다음 인덱싱번호와 맨처음 인덱싱 번호를 뺀것(더하기로 증가하는 값)을 넣어주면 된다
    else: # 아니라면
        # 뒤에 배수로 증가하는 값이기 때문에 
        # 마지막 인덱싱 값에다가 다음 인덱싱번호와 맨처음 인덱싱 번호를 나눈 몫을 곱해준다
        return common[-1] * (common[1] // common[0])
    
def solution(score):
    answer = []

    scores = []
    for i in score:
        scores.append(sum(i)/2)
    scores_1 = sorted(scores, reverse=True)
    for i in scores:
        answer.append(scores_1.index[i]+1)
    return answer

results = solution([[80, 70], [90, 50], [40, 70], [50, 80]])
print(results)