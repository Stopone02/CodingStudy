def solution(s):
    answer = 0
    s = s.split(" ")
    prev = 0
    for e in s:
        if e == 'Z':
            answer -= prev
        else:
            answer += int(e)
            prev = int(e)
    return answer