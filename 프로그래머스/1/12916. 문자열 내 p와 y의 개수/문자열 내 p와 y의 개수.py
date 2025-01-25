def solution(s):
    answer = False
    s = s.lower()
    p = 0
    y = 0
    for i in range(0, len(s)):
        if s[i] == 'p':
            p += 1
        elif s[i] == 'y':
            y += 1
    if y == p:
        answer = True
    return answer