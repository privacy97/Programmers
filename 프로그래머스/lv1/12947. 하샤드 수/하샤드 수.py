def solution(x):
    
    x = str(x)
    
    x_sum = 0
    
    for i in range(len(x)):
        x_sum += int(x[i])
    
    if(int(x) % x_sum == 0):
        answer = True
    else:
        answer = False
    return answer