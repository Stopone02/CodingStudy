def solution(sizes):
    answer = 0
    max_a = 0
    max_b = 0
    for i in range(0, len(sizes)):
        a = sizes[i][0]
        b = sizes[i][1]
        if a > b:
            a, b = b, a
        if a > max_a:
            max_a = a
        if b > max_b:
            max_b = b
    answer = max_a * max_b
    return answer