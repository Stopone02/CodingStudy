def solution(babbling):
    answer = 0
    array = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for k in array:
            i = i.replace(k, '0')
        if i == '0'*len(i):
            answer += 1
    return answer