def solution(arr1, arr2):
    arr1_sum = 0
    arr2_sum = 0
    if len(arr1) == len(arr2):
        for i in range(0, len(arr1)):
            arr1_sum += arr1[i]
        for k in range(0, len(arr2)):
            arr2_sum += arr2[k]
        if arr1_sum > arr2_sum:
            answer = 1
        elif arr1_sum < arr2_sum:
            answer = -1
        else:
            answer = 0
    elif len(arr1) > len(arr2):
        answer = 1
    else:
        answer = -1
    return answer