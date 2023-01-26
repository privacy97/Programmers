def solution(sizes):
    
    big = 0
    small = 0
    
    for i in sizes:
        if max(i) > big:
            big = max(i)
        if min(i) > small:
            small = min(i)
    
    answer = big * small
    return answer