def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        innerlist = []
        for k in range(0, len(arr1[i])):
            innerlist.append(arr1[i][k]+arr2[i][k])
        answer.append(innerlist)
    return answer