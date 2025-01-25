def solution(x):
    answer = False
    xsum = 0
    n = x
    while (True):
        if n == 0:
            break
        xsum += n%10
        n //= 10
    if x%xsum == 0:
        answer = True
    return answer