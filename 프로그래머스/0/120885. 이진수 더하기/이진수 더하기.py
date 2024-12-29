def solution(bin1, bin2):
    answer = ''
    num1 = 0
    num2 = 0
    for i in range(len(bin1)):
        m = len(bin1) - i - 1
        num1 += int(bin1[i]) * (2**m)
    for i in range(len(bin2)):
        m = len(bin2) - i - 1
        num2 += int(bin2[i]) * (2**m)
    number = num1 + num2
    while True:
        answer += str(number%2)
        number //= 2
        if number == 0:
            break
    answer = answer[::-1]
    return answer