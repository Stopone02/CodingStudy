def solution(s):
    answer = ''
    s = s.split(' ')
    print(s)
    for i in range(0, len(s)):
        for k in range(0, len(s[i])):
            if k%2 == 0:
                answer += s[i][k].upper()
            else:
                answer += s[i][k].lower()
        if i != len(s)-1:
            answer += ' '
    return answer