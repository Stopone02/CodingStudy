def solution(myString, pat):
    change_str = ''
    change_pat = ''
    for i in range(0, len(myString)):
        change_str += myString[i].upper()
    for k in range(0, len(pat)):
        change_pat += pat[k].upper()
    if change_pat in change_str:
        answer = 1
    else:
        answer = 0
    return answer