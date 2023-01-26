def solution(n):
    
    result = ''
    
    while n:
        if n % 3:
            result += str(n % 3)
            n = n // 3
        else:
            result += "4"
            n = (n // 3) - 1
    
    result = result[::-1]
    
    return result