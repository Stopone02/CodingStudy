def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(0, len(d)):
        budget -= d[i]
        if budget < 0:
            break
        answer += 1
    return answer