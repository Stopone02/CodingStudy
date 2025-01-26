def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n
    for i in range(n, 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    for k in range(m, n*m+1):
        if k%n == 0 and k%m == 0:
            answer.append(k) 
            break
    return answer