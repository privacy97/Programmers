from collections import Counter

def solution(array):
    answer = Counter(array).most_common(n=2)
    print(answer)
    try:
        if answer[0][1] == answer[1][1]:
            answer = -1
        else:
            answer = answer[0][0]
    except:
        answer = answer[0][0]
            
    
    return answer