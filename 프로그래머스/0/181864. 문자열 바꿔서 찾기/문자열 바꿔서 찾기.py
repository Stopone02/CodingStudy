def solution(myString, pat):
    change = ''
    for i in range(0, len(myString)):
        if myString[i] == 'A':
            change += 'B'
        else:
            change += 'A'
    if pat in change:
        answer = 1
    else:
        answer = 0
    return answer