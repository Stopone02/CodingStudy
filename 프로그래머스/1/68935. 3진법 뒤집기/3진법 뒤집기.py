def solution(n):
    answer = 0
    jinbub3 = ''
    while (True):
        if n == 0:
            break
        jinbub3 += str(n%3)
        n //= 3
    for i in range(len(jinbub3)-1, -1, -1):
        answer += 3**(len(jinbub3)-i-1) * int(jinbub3[i])
    return answer