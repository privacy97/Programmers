def solution(array, n):
    answer = 0
    compare = float('inf')
    for i in array:
        if compare >= abs(i-n):
            if compare == abs(i-n):
                answer = min(i, answer)
            else:
                compare = abs(i-n)
                answer = i
    return answer