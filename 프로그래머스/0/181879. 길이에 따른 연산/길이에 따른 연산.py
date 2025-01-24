def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for i in range(0, len(num_list)):
            answer *= num_list[i]
    return answer