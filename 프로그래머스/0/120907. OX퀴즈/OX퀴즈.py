def solution(quiz):
    answer = []
    for i in quiz:
        array = i.split()
        if array[1] == '+':
            array_answer = int(array[0]) + int(array[2])
            if array_answer == int(array[-1]):
                answer.append("O")
            else:
                answer.append("X")
        if array[1] == '-':
            array_answer = int(array[0]) - int(array[2])
            if array_answer == int(array[-1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer