def solution(lines):
    answer = 0
    lines.sort(key = lambda x:(x[0], x[1]))   
    prevS = lines[0][0]
    prevE = lines[0][1]
    for (start, end) in lines[1:]:
        if start < prevE:
            answer += min(end, prevE) - max(start, prevS)
            prevS = min(end, prevE)
            prevE = max(prevE, end)
        else:
            prevS = start
            prevE = end
    return answer