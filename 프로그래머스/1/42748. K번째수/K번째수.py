def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        numlist = []
        for k in range(commands[i][0]-1, commands[i][1]):
            numlist.append(array[k])
        numlist.sort()
        num = commands[i][2]
        answer.append(numlist[num-1])
    return answer