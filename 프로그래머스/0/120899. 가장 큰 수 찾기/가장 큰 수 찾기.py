def solution(array):
    answer = []
    sorted_array = sorted(array, reverse=True)
    answer.append(sorted_array[0])
    for i in range(0,len(array)):
        if sorted_array[0] == array[i]:
            answer.append(i)
    return answer