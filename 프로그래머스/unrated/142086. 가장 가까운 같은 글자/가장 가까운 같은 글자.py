def solution(s):
    
    s = list(s)
    s_dic = {}
    answer = []
    
    for i in range(len(s)):
        try:
            temp = s_dic.get(s[i])
            answer.append(i-temp)
            s_dic[s[i]] = i
        except:
            answer.append(-1)
            s_dic[s[i]] = i
    
    #print(s_dic)
    return answer