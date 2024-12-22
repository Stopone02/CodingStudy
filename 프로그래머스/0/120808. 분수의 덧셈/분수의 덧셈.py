def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom3 = denom1 * denom2
    numer3 = numer1 * denom2 + numer2 * denom1
    while True:
        check = 0
        for i in range(2,min(denom3, numer3)+1):
            if denom3%i == 0 and numer3%i == 0:
                denom3 = denom3//i
                numer3 = numer3//i
                check = 1
        if check == 0:
            break
    answer.append(numer3)
    answer.append(denom3)
    return answer