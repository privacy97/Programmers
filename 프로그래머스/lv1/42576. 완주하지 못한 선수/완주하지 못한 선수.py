def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    completion.append(0)
    
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    return answer