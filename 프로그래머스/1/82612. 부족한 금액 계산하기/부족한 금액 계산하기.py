def solution(price, money, count):
    ori_price = price
    for i in range(0, count):
        money -= price
        price += ori_price
    if money < 0:
        answer = -money
    else:
        answer = 0   
    return answer