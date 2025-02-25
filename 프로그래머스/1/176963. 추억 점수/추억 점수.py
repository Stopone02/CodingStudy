def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(0, len(name)):
        score[name[i]] = yearning[i]
    for j in range(0, len(photo)):
        sum_score = 0
        for k in photo[j]:
            if k in score:
                sum_score += score[k]
        answer.append(sum_score)
    return answer