def solution(myString):
    answer = ''
    for i in range(0, len(myString)):
        answer += myString[i].lower()
    return answer