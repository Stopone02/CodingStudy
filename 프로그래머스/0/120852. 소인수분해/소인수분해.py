def solution(n):
    answer = []
    array = []
    while True:
        for i in range(2, n+1):
            if n%i == 0:
                array.append(i)
                n //= i
                break
        if n == 1:
            break
    array = set(array)
    answer = list(array)
    answer.sort()
    return answer