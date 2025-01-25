def solution(arr):
    answer = []
    i = 1
    while (True):
        if len(arr) == 1:
            answer.append(-1)
            break
        elif i in arr:
            arr.remove(i)
            answer = arr
            break
        i += 1
    return answer