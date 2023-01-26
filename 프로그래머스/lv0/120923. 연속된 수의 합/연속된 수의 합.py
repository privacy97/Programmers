def solution(num, total):
    answer = []
    if total%num == 0:
        temp = total//num - num//2
        for i in range(num):
            answer.append(temp+i)
    else:
        temp = (total//num + 1) - num//2
        for i in range(num):
            answer.append(temp+i)
    return answer