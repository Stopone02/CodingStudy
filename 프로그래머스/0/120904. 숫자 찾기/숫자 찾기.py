def solution(num, k):
    cnt = 0
    length = 0
    while True:
        length += 1
        mod = num%10
        num = num//10
        print(length, num, mod, cnt)
        if mod == k:
            cnt = length
        if num == 0:
            break
    answer = length - (cnt-1)
    if cnt == 0:
        answer = -1
    return answer