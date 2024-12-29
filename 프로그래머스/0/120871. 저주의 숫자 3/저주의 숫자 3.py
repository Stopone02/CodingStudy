def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += 1
        while True:
            if answer%3 == 0:
                answer += 1
                continue
            elif '3' in str(answer):
                answer += 1
                continue
            break          
    return answer