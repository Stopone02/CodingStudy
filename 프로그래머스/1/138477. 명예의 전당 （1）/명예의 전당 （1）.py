def solution(k, score):
    top = []
    out = []
    for i in range(0, len(score)):
        if len(top) < k:
            top.append(score[i])
        else:
            top.sort()
            if score[i] > top[0]:
                top[0] = score[i]
        top.sort()
        out.append(top[0])
    return out