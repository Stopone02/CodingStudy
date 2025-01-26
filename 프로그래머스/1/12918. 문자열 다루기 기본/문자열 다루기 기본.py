def solution(s):
    answer = False
    count = 0
    if len(s) == 4 or len(s) == 6:
        for i in range(0, len(s)):
            if '0' <= s[i] <= '9':
                count += 1
    if count == len(s):
        answer = True
    return answer