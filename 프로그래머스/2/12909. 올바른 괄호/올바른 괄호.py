def solution(s):
    stack = []
    answer = True
    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                answer = False
                break
            del stack[-1]
    if len(stack) != 0:
        answer = False
    return answer