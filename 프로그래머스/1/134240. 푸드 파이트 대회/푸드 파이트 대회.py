def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] > 1:
            for k in range(0, food[i]//2):
                answer += str(i)
    answer2 = answer
    answer += '0'
    for h in range(len(answer2)-1, -1, -1):
        answer += answer2[h]
    return answer