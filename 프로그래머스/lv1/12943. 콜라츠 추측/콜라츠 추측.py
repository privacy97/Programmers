def solution(num):
    count = 0
    while not(count == 500 or num == 1):
        if num%2 == 1:
            num = num*3 + 1
            count += 1
        else:
            num = int(num/2)
            count += 1
    
    if count == 500:
        count = -1
        
    return count