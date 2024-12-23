def solution(array):
    c_number = []
    for i in set(array):
        c_number.append([i, array.count(i)])
        c_number.sort(key=lambda x:x[1], reverse=True)
        if len(c_number) != 1:
            if c_number[0][1] == c_number[1][1]:
                answer = -1
            else:
                answer = c_number[0][0]
        else:
            answer = c_number[0][0]
    return answer
            