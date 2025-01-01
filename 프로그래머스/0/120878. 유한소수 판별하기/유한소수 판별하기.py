def solution(a, b):
    answer = 1
    i = 1
    j = 1
    while True:
        i += 1
        if a%i == 0 and b%i == 0:
            a //= i
            b //= i
            i = 1
        if i == a or i == b:
            break
    while b>1:
        j += 1
        if b%j == 0:
            if j != 2 and j != 5:
                answer = 2
                break
            b //= j
            j = 1
    return answer