def solution(spell, dic):
    answer = 2
    for i in dic:
        cnt = 0
        for k in spell:
            if k not in i:
                break
            cnt += 1
        if cnt == len(spell):
            answer = 1
            break
    return answer