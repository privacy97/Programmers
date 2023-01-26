def solution(score):
    answer = []
    for i in range(len(score)):
        temp = (score[i][0] + score[i][1]) / 2
        score[i] = temp
        answer.append(temp)
        
    answer.sort(reverse=True)
    #print(score, answer)
    
    rank = [1]
    for i in range(1, len(answer)):
        if answer[i-1] == answer[i]:
            rank.append(rank[i-1])
        else:
            rank.append(i+1)
    
    for i in range(len(score)):
        score[i] = rank[answer.index(score[i])]
    
    return score