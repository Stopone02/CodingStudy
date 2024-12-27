def fact(n):
    if n == 1:
        answer = 1
    else:
        answer = n*fact(n-1)
    return answer

def solution(balls, share):
    if balls == share:
        answer = 1
    else:
        answer = fact(balls)/(fact(balls-share)*fact(share))
    return answer