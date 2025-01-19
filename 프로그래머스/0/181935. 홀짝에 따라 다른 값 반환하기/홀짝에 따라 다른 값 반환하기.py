def solution(n):
    answer = 0
    if n % 2 ==0:
        for i in range(2, n+1, 2):
            answer += i ** 2
    else:
        for k in range(1, n+1, 2):
            answer += k
    return answer