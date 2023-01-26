def solution(s, n):
    s = list(s)
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
        else:
            if i.isupper():
                i = ord(i)
                i += n
                if i > 90:
                    i -= 26
                
            else:
                i = ord(i)
                i += n
                if i > 122:
                    i -= 26
            
            answer += chr(i)
    
    
    return answer