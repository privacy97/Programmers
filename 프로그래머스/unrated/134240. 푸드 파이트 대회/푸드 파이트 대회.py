def solution(food):
    
    answer = ''
    
    for i in range(len(food)):
        # 몫
        n = food[i]//2
        
        # 몫이 0보다 커야함
        if n > 0:
            for j in range(n):
                answer += str(i)
                
    #a = ''.join(reversed(answer))
    
    
    # 기본 + 0 + 뒤집은거
    answer = answer + '0' + answer[::-1]
    
    return answer