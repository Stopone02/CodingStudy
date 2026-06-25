target_check = 0

def cal(lastnum, index, numbers, target):
    global target_check
    if index+1 == len(numbers):
        if target == lastnum:
            target_check += 1
        return
    cal(lastnum + numbers[index+1], index+1, numbers, target)
    cal(lastnum - numbers[index+1], index+1, numbers, target)

def solution(numbers, target):
    global target_check
    cal(numbers[0], 0, numbers, target)
    cal(0-numbers[0], 0, numbers, target)
    return target_check