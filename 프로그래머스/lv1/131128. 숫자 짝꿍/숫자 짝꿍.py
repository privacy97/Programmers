def solution(X, Y):
    
    # 첫번째 시도 X의 데이터로 Y찾기, 시간초과
    '''
    answer = []
    
    X = list(X)
    Y = list(Y)
    X.sort()
    Y.sort()
    
    for i in X:
        if i in Y:
            del Y[Y.index(i)]
            answer.append(i)
    
    answer.sort()
    print(answer)
    
    if len(answer) == 0:
        return '-1'
    elif answer[-1] == '0':
        return '0'
    else:
        answer = ''.join(reversed(answer))
        return answer
    '''
    
    
    '''
    # 숫자 10개에 대해서 탐색 후 삭제, 시간초과
    
    answer = []
    
    X = list(X)
    Y = list(Y)
    
    for i in range(9, -1, -1):
        while True:
            if str(i) in X and str(i) in Y:
                del Y[Y.index(str(i))]
                del X[X.index(str(i))]
                answer.append(str(i))
            else:
                break
    
    print(answer)
    
    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        answer = ''.join(map(str, answer))
        return answer
    '''
    
    
    # 딕셔너리 자료형 사용
    answer = []
    
    X_num_dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    Y_num_dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    
    
    # 해당하는 숫자 추가
    for i in X:
        X_num_dic[i] = X_num_dic[i] + 1
        
    for i in Y:
        Y_num_dic[i] = Y_num_dic[i] + 1
    
    
    # 숫자별로 뽑아내서 저장
    for i in range(9, -1, -1):
        
        X_num = X_num_dic[str(i)] 
        Y_num = Y_num_dic[str(i)]
        
        if X_num == 0 and Y_num == 0:
            continue
        
        for j in range(min(X_num, Y_num)):
            answer.append(str(i))
    
    
    #print(answer)
    
    # 출력
    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        answer = ''.join(map(str, answer))
        return answer
    
    