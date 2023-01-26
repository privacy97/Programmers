def solution(survey, choices):
    MBTI = {'R': 0, 'T': 0,
            'C': 0, 'F': 0,
            'J': 0, 'M': 0,
            'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        temp = choices[i]-4
        if temp > 0:
            MBTI[survey[i][1]] += temp
        elif temp < 0:
            MBTI[survey[i][0]] += abs(temp)
    
    #print(MBTI)
    
    answer = ''
    if MBTI['R'] >= MBTI['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if MBTI['C'] >= MBTI['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if MBTI['J'] >= MBTI['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if MBTI['A'] >= MBTI['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer