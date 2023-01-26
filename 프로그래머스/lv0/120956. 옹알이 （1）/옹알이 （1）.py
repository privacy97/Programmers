def solution(babbling):
    
    bab_list = ['aya', 'ye', 'woo', 'ma']
    
    answer = 0
    
    for i in babbling:
        for j in bab_list:
            # 문자열안에 있으면 0으로 바꿈
            i = i.replace(j,"0").strip()
        
        print(i)
        # 숫자로 바꿨을때 오류나면 패스
        try:
            i = int(i)
            answer += 1
        except:
            continue

    return answer