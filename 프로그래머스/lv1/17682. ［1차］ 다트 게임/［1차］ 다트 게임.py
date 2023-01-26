def solution(dartResult):
    
    dartResult = list(dartResult)
    #print(dartResult)
    score = []
    temp = 0
    
    for i, dart in enumerate(dartResult):
        if dart == 'S':
            temp = int(dartResult[i-1])
            if temp == 0:
                try:
                    temp = int(dartResult[i-2]+dartResult[i-1])
                except:
                    temp = int(dartResult[i-1])
            temp = temp**1
            score.append(temp)
            
        elif dart == 'D':
            temp = int(dartResult[i-1])
            if temp == 0:
                try:
                    temp = int(dartResult[i-2]+dartResult[i-1])
                except:
                    temp = int(dartResult[i-1])
            temp = temp**2
            score.append(temp)
            
        elif dart == 'T':
            temp = int(dartResult[i-1])
            if temp == 0:
                try:
                    temp = int(dartResult[i-2]+dartResult[i-1])
                except:
                    temp = int(dartResult[i-1])
            temp = temp**3
            score.append(temp)
            
        elif dart == '#':
            score[-1] *= (-1)
            
        elif dart == '*':
            if len(score) == 3:
                for i in range(1,len(score)):
                    score[i] *= 2
            else:
                for i in range(len(score)):
                    score[i] *= 2
        
    #print(score)
    answer = sum(score)
    
    return answer