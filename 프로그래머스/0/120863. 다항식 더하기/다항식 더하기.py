def solution(polynomial):
    x = 0
    num = 0
    polynomial = polynomial.split(' + ')
    for i in polynomial:
        if 'x' in i:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[0:-1])
        else:
            num += int(i)
    if x > 1:
        if num == 0:
            answer = f"{x}x"
        else:
            answer = f"{x}x + {num}"
    elif x == 0:
        answer = f"{num}"
    else:
        if num == 0:
            answer = f"x"
        else:
            answer = f"x + {num}"
    return answer