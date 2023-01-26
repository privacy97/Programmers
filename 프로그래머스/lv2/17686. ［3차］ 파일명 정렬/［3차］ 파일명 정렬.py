def solution(files):
    
    for i in range(len(files)):
        temp_list = []
        index = 0
        count = 0
        
        for j in range(len(files[i])):
            if (ord(files[i][j]) >= 48 and ord(files[i][j]) <= 57 and count == 0):
                if j == (len(files[i])-1):
                    temp_list.append(files[i][index:j].lower())
                    temp_list.append(int(files[i][j]))
                    temp_list.append(i)
                    temp_list.append(files[i])
                    files[i] = temp_list
                    break
                
                temp_list.append(files[i][index:j].lower())
                index = j
                count = 1
                
            elif ((not(ord(files[i][j]) >= 48 and ord(files[i][j]) <= 57) or (j - index) == 5) and count == 1):
                temp_list.append(int(files[i][index:j]))
                temp_list.append(i)
                temp_list.append(files[i])
                files[i] = temp_list
                break
            
            elif j == (len(files[i])-1):
                    temp_list.append(int(files[i][index:]))
                    temp_list.append(i)
                    temp_list.append(files[i])
                    files[i] = temp_list
    
    print(files)
    files.sort()
    
    answer = []
    
    for i in files:
        answer.append(i[3])
    
    return answer