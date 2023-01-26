def solution(s):
    temp = len(s)//2
    if len(s)%2 == 0:
        answer = s[temp-1:temp+1]
    else:
        answer = s[temp]
    return answer