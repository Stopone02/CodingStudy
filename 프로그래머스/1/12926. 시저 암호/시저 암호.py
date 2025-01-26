def solution(s, n):
    answer = ''
    for i in range(0, len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if s[i].islower() == True:
                if ord(s[i]) + n > ord('z'):
                    answer += chr(ord(s[i]) + n - (ord('z')-ord('a'))-1)
                else:
                    answer += chr(ord(s[i]) + n)
            else:
                if ord(s[i]) + n > ord('Z'):
                    answer += chr(ord(s[i]) + n - (ord('Z')-ord('A'))-1)
                else:
                    answer += chr(ord(s[i]) + n)        
    return answer