def solution(n):
    n = n**(1/2)
    if int(n) == n:
        answer = 1
    else:
        answer = 2
    return answer