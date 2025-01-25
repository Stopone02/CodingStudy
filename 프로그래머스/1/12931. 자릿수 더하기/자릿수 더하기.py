def solution(n):
    answer = 0
    while (True):
        if n == 0:
            break
        answer += n%10
        n //= 10
    return answer