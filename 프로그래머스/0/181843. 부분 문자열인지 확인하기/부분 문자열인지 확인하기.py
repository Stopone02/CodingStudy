def solution(my_string, target):
    for i in range(0, len(my_string)):
        if my_string[i:i+len(target)] == target:
            answer = 1
            break
        else:
            answer = 0
    return answer