def solution(my_str, n):
    answer = []
    i = 0
    while True:
        answer.append(my_str[i:i+n])
        i += n
        if i > len(my_str) or i == len(my_str):
            break
    return answer