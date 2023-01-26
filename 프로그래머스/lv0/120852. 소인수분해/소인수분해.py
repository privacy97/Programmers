def solution(n):
    answer = []
    while n != 1:
        count = 2
        while True:
            if n % count == 0:
                answer.append(count)
                n = n // count
                count = 2
                break
            else:
                count += 1
    return list(dict.fromkeys(answer))