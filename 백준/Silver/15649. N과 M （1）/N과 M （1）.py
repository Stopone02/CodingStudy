N, M = map(int, input().split())

array = []
combination = []
def DFS(num, array, M):
    global combination
    if num >= M:
        for h in combination:
            print(h, end=' ')
        print()
    else:
        for k in range(1, len(array)+1):
            if k not in combination:
                combination.append(array[k-1])
                DFS(num+1, array, M)
                del combination[-1]

def solution(N, M):
    for i in range(1, N+1):
        array.append(i)
    DFS(0, array, M)

solution(N, M)