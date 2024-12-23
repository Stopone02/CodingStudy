def solution(n):
    number = 0
    while True:
        number += 1
        if n*number%6 == 0:
            answer = n*number//6
            break
    return answer