N, M = map(int, input().split())

array = []
combination = []

def DFS(num, array, M):
    global combination
    if num >= M:
        for k in combination:
            print(k, end=' ')
        print()
    else:
        for h in array:
            combination.append(h)
            DFS(num+1, array, M)
            del combination[-1]
def solution(N, M):
    for i in range(1, N+1):
        array.append(i)
    DFS(0, array, M)

solution(N, M)