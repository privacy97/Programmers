def solution(before, after):
    
    before = list(before)
    before.sort()
    after = list(after)
    after.sort()
    
    if before == after:
        answer = 1
    else:
        answer = 0
        
    return answer