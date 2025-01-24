def solution(num_list):
    num = 0
    for i in range(0, len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
        else:
            num += 1
    if num == len(num_list):
        answer = -1
    return answer