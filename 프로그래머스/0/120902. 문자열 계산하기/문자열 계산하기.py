def solution(my_string):
    my_string = my_string.split()
    i = 1
    answer = int(my_string[0])
    while True:
        if my_string[i] == "+":
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
        if i == len(my_string)-2:
            break
        i += 2
    return answer