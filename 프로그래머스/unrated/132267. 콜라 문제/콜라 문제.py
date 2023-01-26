def solution(a, b, n):
    
    answer = 0
    
    # n을 a로 나눌때의 나머지
    rem = 0
    
    while n > 0:
        # N과 이전결과의 나머지를 더한 수를 a로 나눔, 곱하기 b
        temp = ((n + rem) // a) * b
        
        # N과 이전결과의 나머지를 더한 수를 a로 나눈 나머지 저장
        rem = (n + rem) % a
        
        # 결과를 n에 저장
        n = temp
        
        # 결과를 답에 추가
        answer += temp
    
    
    return answer