def solution(numbers, n):
    answer = 0
    for i in range(0, len(numbers)):
        if answer > n:
            break
        answer += numbers[i]
    return answer