def solution(num_list, n):
    answer = []
    for i in range(n, len(num_list)):
        answer.append(num_list[i])
    for k in range(0, n):
        answer.append(num_list[k])
    return answer