def solution(s):
    answer = ""
    answer += s[0].upper()
    for i in range(1, len(s)):
        if s[i] == ' ':
            answer += ' '
        elif s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer