def solution(s):
    answer = ""
    answer += s[0].upper()
    for i in range(1, len(s)):
        # 오룝다 오룝지
        # 아이디어 뱅크씨 다시 아이디어를 떠올려봐 데굴데굴~ 뱅크씨 지굼 머리 아야라서 안대
        # 길이가 1 이상이니까 첫번째 글자는 무조건 대문자로 만들고 시작하쟈
        # 공백문자면 그냥 공백문자가 나오면 되나? 그런것같오
        if s[i] == ' ':
            answer += ' '
        elif s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer
"""
    모지 왜 문제가 생길까
    왓츠 더 매럴
    음 예상대로군
    split이 내 생각대로 안되네 ㅠㅠ
    애기가 한 것처럼 하는게 맞겠오
"""