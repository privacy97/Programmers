def solution(s):
    s = s.upper()
    answer = False
    if s.count('Y') == s.count('P'):
        answer = True
    return answer