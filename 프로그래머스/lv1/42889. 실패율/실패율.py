def solution(N, stages):
    
    cnt = len(stages)
    fail = {}
    
    for i in range(1, N+1):
        
        user = stages.count(i)
        
        if cnt == 0:
            fail[i] = 0
        else:
            fail[i] = (user/cnt)
            cnt = cnt - user
    
    fail = sorted(fail.items(), key = lambda item: item[1], reverse = True)
    
    answer = []
    for i in fail:
        answer.append(i[0])
    
    return answer