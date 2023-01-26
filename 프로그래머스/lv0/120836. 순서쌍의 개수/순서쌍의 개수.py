def solution(n):
    answer = 0
    for i in range(1,int(n**(1/2))+1):
        if n%i == 0:
            answer += 1
    answer *= 2
    if n**(1/2) == int(n**(1/2)):
        answer -= 1
    return answer