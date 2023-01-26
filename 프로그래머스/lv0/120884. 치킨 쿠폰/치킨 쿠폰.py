def solution(chicken):
    if chicken == 0:
        return 0
    answer = chicken//9
    if chicken%9 == 0:
        answer -= 1
    return answer