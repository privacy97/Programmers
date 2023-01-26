def solution(n):
    answer = 0
    for i in range(n):
        while True:
            if str(answer).find('3') >= 0:
                answer = int(answer) + 1
            elif int(answer) % 3 == 0:
                answer = int(answer) + 1
            else:
                answer = int(answer) + 1
                break
    return answer - 1