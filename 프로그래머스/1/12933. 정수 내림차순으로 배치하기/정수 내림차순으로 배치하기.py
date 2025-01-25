def solution(n):
    nlist = []
    answer = []
    while (True):
        if n == 0:
            break
        nlist.append(str(n%10))
        n //= 10
    nlist.sort(reverse=True)
    answer = "".join(nlist)
    return int(answer)