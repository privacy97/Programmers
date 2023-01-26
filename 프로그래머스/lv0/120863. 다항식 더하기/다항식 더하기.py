def solution(polynomial):
    answer = polynomial.split(' ')
    
    x = 0
    num = 0
    
    for i in answer:
        if i == 'x':
            x += 1
        elif i[-1] == 'x':
            x += int(i[:-1])
        else:
            try:
                num += int(i)
            except:
                continue
    
    if x == 0:
        answer = str(num)
    elif num == 0:
        if x == 1:
            answer = 'x'
        else:
            answer = str(x) + 'x'
    else:
        if x == 1:
            answer = 'x + ' + str(num)
        else:
            answer = str(x) + 'x + ' + str(num)
    return answer