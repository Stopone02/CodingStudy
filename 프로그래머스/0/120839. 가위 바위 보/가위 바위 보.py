def solution(rsp):
    answer = ''
    for i in rsp:
        if int(i) == 2:
            answer += str(0)
        elif int(i) == 0:
            answer += str(5)
        else:
            answer += str(2)
    return answer