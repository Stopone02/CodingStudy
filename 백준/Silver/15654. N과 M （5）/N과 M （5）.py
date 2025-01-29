N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
combination = []
def DFS(num, array, M):
    global combination
    if num >= M:
        for i in combination:
            print(i, end=' ')
        print()
    else:
        for j in range(0, len(array)):
            if array[j] not in combination:
                combination.append(array[j])
                DFS(num+1, array, M)
                del combination[-1]
def solution(N, M):
    DFS(0, array, M)

solution(N, M)