def solution(strings, n):
    
    s_list = []
    for i in range(len(strings)):
        s_list.append([strings[i][n], strings[i]])
    
    print(s_list)
    s_list.sort()
    
    answer = []
    for i in range(len(s_list)):
        answer.append(s_list[i][1])
    
    return answer