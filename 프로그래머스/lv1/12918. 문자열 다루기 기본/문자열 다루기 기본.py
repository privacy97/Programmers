def solution(s):
    try:
        answer = int(s)
        answer = True
        if not(len(s) == 4 or len(s) == 6):
            answer = False
    except:
        answer = False
    return answer