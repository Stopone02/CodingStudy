def solution(order):
    answer = 0
    while True:
        if order%10 == 3 or order%10 == 6 or order%10 == 9:
            answer += 1
        order = order//10
        if order == 0:
            break
    return answer