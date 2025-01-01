def solution(score):
    answer = []
    score_ave = []
    for i in score:
        score_ave.append((i[0]+i[1])/2)
    for i in score_ave:
        cnt = 1
        for k in score_ave:
            if i < k:
                cnt += 1
        answer.append(cnt)
    return answer