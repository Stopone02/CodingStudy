N, M = map(int, input().split())

array = []
combination = []

def DFS(num, start, array, M):
    global combination
    if num >= M:
        for j in combination:
            print(j, end=' ')
        print()
    else:
        for k in range(start, len(array)):
            combination.append(array[k])
            DFS(num+1, k, array, M)
            del combination[-1]
def solution(N, M):
    for i in range(1, N+1):
        array.append(i)
    DFS(0, 0, array, M)

solution(N, M)