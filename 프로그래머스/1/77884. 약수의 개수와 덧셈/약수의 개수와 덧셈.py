def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        num = 0
        for k in range(1, i+1):
            if i%k == 0:
                num += 1
        if num%2 == 0:
            answer += i
        else:
            answer -= i      
    return answer