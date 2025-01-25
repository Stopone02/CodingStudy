def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)-4):
        answer += '*'
    for k in range(len(phone_number)-4, len(phone_number)):
        answer += phone_number[k]
    return answer