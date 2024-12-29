def solution(numbers):
    eng = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in eng:
        if i in numbers:
            numbers = numbers.replace(i, eng[i])
    return int(numbers)