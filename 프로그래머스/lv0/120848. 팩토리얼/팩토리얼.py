def solution(n):
    answer = 1
    count = 1
    
    while answer <= n:
        count += 1
        answer = count*answer

    return count-1