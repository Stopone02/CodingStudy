def solution(myString):
    answer = ''
    for i in range(0, len(myString)):
        if myString[i] < 'l':
            answer += 'l'
        else:
            answer += myString[i]
    return answer