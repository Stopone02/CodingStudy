def solution(s):
    answer = []
    for i in range(0, len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            for k in range(i-1, -1, -1):
                if s[i] == s[k]:
                    answer.append(i-k)
                    break
    return answer