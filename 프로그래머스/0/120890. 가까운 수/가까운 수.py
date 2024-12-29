def solution(array, n):
    gap = []
    for i in array:
        gap.append(abs(i-n))
    gap.sort()
    answer = n - gap[0]
    if answer not in array:
        answer = gap[0] + n
    return answer