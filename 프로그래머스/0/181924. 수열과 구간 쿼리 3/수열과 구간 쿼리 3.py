def solution(arr, queries):
    for i in range(0, len(queries)):
        arr[queries[i][0]], arr[queries[i][1]] = arr[queries[i][1]], arr[queries[i][0]]
    return arr