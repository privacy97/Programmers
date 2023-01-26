def solution(k, score):
    
    hall = []
    answer = []
    
    for i in score:
        hall.append(i)
        hall.sort()
        
        if len(hall) > k:
            hall.pop(0)
        
        answer.append(hall[0])
        
    return answer