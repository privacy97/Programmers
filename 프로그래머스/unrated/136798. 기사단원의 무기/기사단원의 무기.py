def solution(number, limit, power):
    
    answer = []
    
    for i in range(1, number+1):
        
        n = 0
        # 제곱근을 이용한 약수 구하기 방법
        for j in range(1, int(i**(1/2))+1):
            if (i%j == 0):
                n += 1
                if ((j**2) != i): 
                    n += 1
        
        if n > limit:
            answer.append(power)
        else:
            answer.append(n)

    return sum(answer)