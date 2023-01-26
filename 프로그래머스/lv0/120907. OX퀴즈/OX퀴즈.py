def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        if eval(quiz[i][:(quiz[i].find('=')-1)]) == int(quiz[i][(quiz[i].find('=')+2):]):
            answer.append("O")
        else:
            answer.append("X")
    return answer