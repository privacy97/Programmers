def solution(ingredient):
    
    answer = 0
    temp = []
    
    for i in ingredient:
        temp.append(i)
        if temp[-4:]==[1,2,3,1]:
            answer += 1
            for i in range(4):
                temp.pop()

    return answer