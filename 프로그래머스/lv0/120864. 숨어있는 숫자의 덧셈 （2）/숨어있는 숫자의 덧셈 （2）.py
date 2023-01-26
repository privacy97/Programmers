def solution(my_string):
    answer = 0
    temp = ''
    for i in list(my_string):
        if ord(i) >= 48 and ord(i) <= 57:
            temp += i
        else:
            try:
                answer += int(temp)
                temp = ''
            except:
                continue
    try:
        answer += int(temp)
    except:
        pass
    
    return answer