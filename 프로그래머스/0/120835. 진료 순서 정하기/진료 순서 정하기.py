def solution(emergency):
    answer = []
    sorted_array = sorted(emergency, reverse=True)
    for i in emergency:
        for k in range(0, len(sorted_array)):
            if i == sorted_array[k]:
                answer.append(k+1)
    return answer