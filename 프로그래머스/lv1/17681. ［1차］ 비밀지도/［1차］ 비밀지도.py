def solution(n, arr1, arr2):
    
    answer = []
    
    for i in range(n):
        a = str(bin(arr1[i])[2:])
        b = str(bin(arr2[i])[2:])
        
        temp = ''
        for i in range(n):
            ai = i - (n - len(a))
            bi = i - (n - len(b))
            
            if ai < 0:
                ai = 0
            else:
                ai = int(a[ai])
                
            if bi < 0:
                bi = 0
            else:
                bi = int(b[bi])
            
            if ai == 1 or bi == 1:
                temp += '#'
            else:
                temp += ' '
        
        answer.append(temp)
    
    return answer