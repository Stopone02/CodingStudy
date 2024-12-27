def solution(n):
    answer = 1
    fact = 1
    while True:
        fact = fact*(answer+1)
        if fact > n:
            break
        answer += 1
    return answer