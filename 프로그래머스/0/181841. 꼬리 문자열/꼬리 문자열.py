def solution(str_list, ex):
    answer = ''
    for i in range(0, len(str_list)):
        if ex not in str_list[i]:
            answer += str_list[i]
    return answer