def solution(A, B):
    answer = -1
    list_A = list(A)
    check = False
    for i in range(0, len(A)):
        answer += 1
        if ''.join(list_A) == B:
            check = True
            break
        last = list_A[-1]
        del list_A[-1]
        list_A.insert(0,last)
    if check == False:
        answer = -1
    return answer