combination = [] 
answer = 0

def DFS(num, start, number):
    global answer, combination
    if num >= 3:
        if sum(combination) == 0:
            answer += 1
    else:
        for i in range(start, len(number)):
            combination.append(number[i])
            DFS(num+1, i+1, number)
            del combination[-1]
            
def solution(number):
    global answer
    DFS(0, 0, number)
    return answer