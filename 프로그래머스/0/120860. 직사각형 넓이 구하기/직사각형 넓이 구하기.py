def solution(dots):
    answer = 0
    for i in range(1, 4):
        if dots[0][0] != dots[i][0] and dots[0][1] != dots[i][1]:
            length = abs(dots[i][0] - dots[0][0])
            height =abs(dots[i][1] - dots[0][1])
            answer = length * height
            break
    return answer