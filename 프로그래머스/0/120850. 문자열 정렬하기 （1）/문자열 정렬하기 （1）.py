def solution(my_string):
    answer = []
    number = '0123456789'
    for i in my_string:
        if i in number:
            answer.append(int(i))
    answer.sort()
    return answer