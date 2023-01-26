def solution(s):
    
    s = list(s)
    temp = []
    recode = 0
    cnt = 0
    
    for i in range(len(s)):
        if cnt == 0 and s[i] == ' ':
            temp.append(s[recode:i])
            recode = i
            cnt = 1
        
        if cnt == 1 and s[i] != ' ':
            temp.append(s[recode:i])
            recode = i
            cnt = 0
            
    temp.append(s[recode:len(s)])
    #print(temp)
    
    for i in range(len(temp)):    
        for j in range(len(temp[i])):
            if j%2 == 1:
                temp[i][j] = temp[i][j].lower()
            else:
                temp[i][j] = temp[i][j].upper()
        temp[i] = ''.join(temp[i])
        
    return ''.join(temp)