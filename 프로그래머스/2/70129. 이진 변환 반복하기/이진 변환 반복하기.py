def solution(s):
    count = 0
    del0 = 0
    while len(s) > 1:
        nexts = [] 
        for i in s:
            if i != '0':
                nexts.append(i)
            else:
                del0 += 1 
        length = len(nexts)
        binary = ''
        while length > 0:
            binary = str(length % 2) + binary 
            length = length // 2
        s = binary 
        count += 1 
    return count, del0
