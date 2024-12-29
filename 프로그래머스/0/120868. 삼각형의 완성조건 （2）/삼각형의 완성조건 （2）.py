def solution(sides):
    answer = 0
    sides.sort()
    side = sides[0] + sides[1] - 1
    while True:
        answer += 1
        side -= 1
        if side + sides[0] == sides[1]:
            break
    return answer