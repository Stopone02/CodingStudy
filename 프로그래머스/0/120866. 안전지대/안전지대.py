def solution(board):
    answer = 0
    array = [[0 for _ in range(len(board))] for _ in range(len(board))]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(0, len(board)):
        for k in range(0, len(board)):
            if board[i][k] == 1:
                array[i][k] = 1
                for j in range(0, 8):
                    nx = i + dx[j]
                    ny = k + dy[j]
                    if nx > -1 and ny > -1 and nx < len(board) and ny < len(board):
                        array[nx][ny] = 1
    for i in range(0, len(array)):
        for k in range(0, len(array)):
            if array[i][k] == 0:
                answer += 1
    return answer