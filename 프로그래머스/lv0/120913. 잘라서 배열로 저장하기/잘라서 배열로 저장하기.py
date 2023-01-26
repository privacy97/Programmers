def solution(my_str, n):
    #answer = [my_str[(i-n+1):(i+1)] for i in range(n-1, len(my_str), n)]
    answer = []
    for i in range(n-1, len(my_str), n):
        answer.append(my_str[(i-n+1):(i+1)])
    if len(my_str) % n != 0:
        answer.append(my_str[len(my_str)-(len(my_str) % n):])
    return answer