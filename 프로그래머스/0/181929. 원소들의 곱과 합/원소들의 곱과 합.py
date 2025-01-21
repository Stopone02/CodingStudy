def solution(num_list):
    num_mut = 1
    num_sum = 0
    for i in num_list:
        num_mut *= i
        num_sum += i
    if num_mut < num_sum**2:
        answer = 1
    else:
        answer = 0
    return answer