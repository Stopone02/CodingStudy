def solution(keyinput, board):
    answer = [0,0]
    limit_x = board[0]//2
    limit_y = board[1]//2
    dic = {"left":[-1,0], "right":[1,0], "up":[0,1], "down":[0,-1]}
    for i in keyinput:
        answer[0] += dic[i][0]
        answer[1] += dic[i][1]
        if answer[0] > limit_x:
            answer[0] = limit_x
        if answer[0] < -limit_x:
            answer[0] = -limit_x
        if answer[1] > limit_y:
            answer[1] = limit_y
        if answer[1] < -limit_y:
            answer[1] = -limit_y
    return answer