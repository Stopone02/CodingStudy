def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    cnt = 1
    if len(s) == 1:
        answer += s[0]
    else:
        if s[0] != s[1]:
            answer += s[0]
        while True:
            if s[cnt] != s[cnt-1] and s[cnt] != s[cnt+1]:
                answer += s[cnt]
            cnt += 1
            if cnt == len(s)-1:
                break
        if s[-1] != s[-2]:
            answer += s[-1]
    return answer