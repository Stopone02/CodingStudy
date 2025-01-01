def solution(numlist, n):
    answer = []
    array = []
    for i in numlist:
        array.append([abs(i-n), i])
    array.sort(key=lambda x:(x[0],-x[1]))
    for (d, e) in array:
        answer.append(e)
    return answer