def solution(arr, intervals):
    answer = []
    for i in range(0, len(intervals)):
        for k in range(intervals[i][0], intervals[i][1]+1):
            answer.append(arr[k])
    return answer