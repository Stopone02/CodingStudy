def solution(s):
    slist = list(s)
    answer = ''
    slist.sort(reverse=True)
    for i in range(0, len(slist)):
        answer += slist[i]
    return answer