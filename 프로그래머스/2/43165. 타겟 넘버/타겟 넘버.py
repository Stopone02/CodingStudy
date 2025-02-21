answer = 0
n = []

def dfs(a, sum_a, target):
    global answer, n
    if a >= len(n):
        if sum_a == target:
            answer += 1
    else:
        for i in range(1, 3):
            dfs(a+1, sum_a + (-1)**i * n[a], target)
            
    
         
def solution(numbers, target):
    global answer, n
    answer = 0
    n = numbers
    dfs(0, 0, target)
    return answer