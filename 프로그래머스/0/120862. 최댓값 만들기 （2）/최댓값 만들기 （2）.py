def solution(numbers):
    array = []
    for i in numbers:
        numbers.remove(i)
        for k in numbers:
            array.append(i*k)
    array.sort(reverse=True)
    return array[0]