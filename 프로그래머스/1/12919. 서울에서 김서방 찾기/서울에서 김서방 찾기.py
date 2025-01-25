def solution(seoul):
    answer = '김서방은 '
    for i in range(0, len(seoul)):
        if seoul[i] == 'Kim':
            answer += str(i)
    answer += '에 있다'
    return answer