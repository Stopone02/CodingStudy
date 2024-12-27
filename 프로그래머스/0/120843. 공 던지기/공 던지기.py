def solution(numbers, k):
    pointer = 0 + (2 * (k - 1))
    answer = numbers[pointer % len(numbers)]
    return answer