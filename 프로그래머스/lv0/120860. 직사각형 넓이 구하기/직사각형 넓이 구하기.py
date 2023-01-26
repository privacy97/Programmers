def solution(dots):
    temp = dots[0]
    answer = []
    for i in range(1, 4):
        answer.append(((temp[1] - dots[i][1])**2 + (temp[0] - dots[i][0])**2)**(1/2))
        answer.sort()
    return answer[0]*answer[1]