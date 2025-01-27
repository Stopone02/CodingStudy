def solution(arr, delete_list):
    answer = []
    for i in range(0, len(delete_list)):
        if delete_list[i] in arr:
            arr.remove(delete_list[i])
    answer = arr
    return answer