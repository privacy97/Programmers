def solution(n):
    
    
    thr = ''
    while n > 0:
        temp = n%3
        thr += str(temp)
        n = n//3
    
    answer = (int(thr,3))
    return answer