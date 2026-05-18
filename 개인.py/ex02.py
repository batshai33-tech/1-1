def solution(score):
    answer = []

    scores = []
    for i in score:
        scores.append(sum(i)/2)
    scores_1 = sorted(scores, reverse=True)
    for i in scores:
        answer.append(scores_1.index(i)+1)
    return answer

results = solution([[80, 70], [90, 50], [40, 70], [50, 80]])
print(results)