def solution(num, k):
    num = list(str(num))
    try:
        answer = num.index(str(k))+1
    except:
        answer = -1
    return answer