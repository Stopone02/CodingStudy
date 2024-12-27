def solution(n):
    answer = 2
    i = 1
    while True:
        if n//i == i and n%i ==0:
            answer = 1
            break
        if i > n:
            break
        i += 1
    return answer