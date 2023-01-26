def solution(today, terms, privacies):
    
    answer = []
    today = int(''.join(today.split('.')))
    terms_dic = {}
    
    for i in terms:
        a, b = i.split()
        terms_dic[a] = int(b)
    
    #today는 숫자, terms_dic은 ex){'A': 6}
    #print(today, terms_dic)
    
    for i, privacies in enumerate(privacies):
        day, term = privacies.split()
        day = list(map(int, day.split('.')))
        term_y = terms_dic[term] // 12
        term_m = terms_dic[term] % 12
        
        day[0] += term_y
        day[1] += term_m
        
        if day[1] > 12:
            day[0] += 1
            day[1] -= 12
        
        d_day = ''
        
        for j in day:
            j = str(j)
            if len(j) == 1:
                j = '0' + j
            d_day += j
        
        if today >= int(d_day):
            answer.append(i+1)
    
    return answer