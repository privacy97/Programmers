def solution(lines):
    answer_dic = {}
    for i in lines:
        for j in range(i[0]+1, i[1]+1):
            try:
                answer_dic[j] += 1
            except:
                answer_dic[j] = 1
    print(answer_dic)
    answer = len(answer_dic) - list(answer_dic.values()).count(1)
    return answer