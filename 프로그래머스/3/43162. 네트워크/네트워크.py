graph = 0

def dfs(node, visit):
    global graph
    for j in range(0, len(graph[node])):
        if graph[node][j] == 1 and visit[j] != 1:
            visit[j] = 1
            dfs(j, visit)

def solution(n, computers):
    global graph
    graph = computers
    answer = 0
    visit = [0 for _ in range(0, n)]
    for i in range(0, n):
        if visit[i] == 0:
            dfs(i, visit)
            answer += 1
    return answer