def solution(board, moves):
    
    answer = 0
    box = []
    
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                try:
                    if box[-1] == j[i-1]:
                        box.pop(-1)
                        answer += 2
                        j[i-1] = 0
                        break
                    else:
                        box.append(j[i-1])
                        j[i-1] = 0
                        break
                except:
                    box.append(j[i-1])
                    j[i-1] = 0
                    break
    
    return answer