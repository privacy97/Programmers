def solution(age):
    answer = ''
    a_dic = 'abcdefghij'
    age = str(age)
    
    for i in age:
        answer += a_dic[int(i)]

    return answer