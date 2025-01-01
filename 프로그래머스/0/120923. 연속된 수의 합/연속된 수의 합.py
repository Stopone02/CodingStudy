def solution(num, total):
    answer = []
    for i in range(-10000, 10000):
        sum_num = 0
        for k in range(i, i+num):
            sum_num += k
        if sum_num == total:
            for k in range(i, i+num):
                answer.append(k)
            break
    return answer