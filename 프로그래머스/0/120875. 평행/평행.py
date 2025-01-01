def solution(dots):
    answer = 0
    
    # (1, 2) (3, 4)
    grad1 = (dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0])
    grad2 = (dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0])
    print("#1", grad1, grad2)
    if grad1 == grad2:
        answer = 1
    
    # (1, 3) (2, 4)
    grad1 = (dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0])
    grad2 = (dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0])
    print("#2", grad1, grad2)
    if grad1 == grad2:
        answer = 1
    
    # (1, 4) (2, 3)
    grad1 = (dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0])
    grad2 = (dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0])
    print("#3", grad1, grad2)
    if grad1 == grad2:
        answer = 1
    
    return answer