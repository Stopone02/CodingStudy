def solution(my_string):
    answer = 0
    string = ''
    for i in my_string:
        if ord(i) > 47 and ord(i) < 58:
            string += i
        else:
            string += ' '
    string = string.split()
    for i in string:
        if len(i) != 0:
            answer += int(i)
    return answer