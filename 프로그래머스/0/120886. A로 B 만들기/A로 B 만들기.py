def solution(before, after):
    answer = 0
    before = list(before)
    after = list(after)
    for i in before:
        if i in after:
            after.remove(i)
        if len(after) == 0:
            answer = 1
    return answer