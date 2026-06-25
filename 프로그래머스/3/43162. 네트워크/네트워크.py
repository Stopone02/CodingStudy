check = []
answer = 0

def network(index, computers):
    global check, answer
    check[index] = 1
    for i in range(len(computers)):
        if index == i:
            continue
        if computers[index][i] == 1:
            if check[i] == 0:
                network(i, computers)

def solution(n, computers):
    global check, answer
    for i in range(n):
        check.append(0)
    for i in range(n):
        if check[i] == 0:
            answer += 1
            network(i, computers)
    return answer
    