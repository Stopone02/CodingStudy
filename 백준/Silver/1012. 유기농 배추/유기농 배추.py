import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(N, M, k, h, batt):
    global dx, dy, visited
    for l in range(0, 4):
        nx = k + dx[l]
        ny = h + dy[l]
        if 0<=nx<N and 0<=ny<M:
            if batt[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(N, M, nx, ny, batt)

T = int(input())
for i in range(0, T):
    answer = 0
    M, N, K = map(int, input().split())
    batt = [[0 for _ in range(M)]for _ in range(N)]
    visited = [[0 for _ in range(M)]for _ in range(N)]
    for j in range(0, K):
        X, Y = map(int, input().split())
        batt[Y][X] = 1
    for k in range(0, N):
        for h in range(0, M):
            if batt[k][h] == 1 and visited[k][h] == 0:
                DFS(N, M, k, h, batt)
                answer += 1
    print(answer)

