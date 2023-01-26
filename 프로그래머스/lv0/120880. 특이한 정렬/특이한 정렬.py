def solution(numlist, n):
    answer = []
    for i in numlist:
        temp = [abs(i-n), i]
        answer.append(temp)
        
    answer = sorted(answer, key=lambda x: (x[0], -x[1]))
    for i in range(len(answer)):
        answer[i] = answer[i][1]
        
    return answer