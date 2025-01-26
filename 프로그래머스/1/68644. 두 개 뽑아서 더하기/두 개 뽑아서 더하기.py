def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for k in range(0, len(numbers)):
            if i != k:
                if numbers[i]+numbers[k] not in answer:
                    answer.append(numbers[i]+numbers[k])
    answer.sort()
    return answer