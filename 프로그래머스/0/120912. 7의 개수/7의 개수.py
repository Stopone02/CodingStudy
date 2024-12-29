def solution(array):
    answer = 0
    for i in array:
        while True:
            if i%10 == 7:
                answer += 1
            if i//10 == 0:
                break 
            i //= 10
    return answer