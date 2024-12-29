def solution(i, j, k):
    answer = 0
    for i in range(i, j+1):
        string = str(i)
        for l in string:
            if int(l) == k:
                answer += 1
    return answer