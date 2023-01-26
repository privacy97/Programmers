def solution(A, B):
    answer = 0
    while A != B:
        A = A[-1]+A[0:len(A)-1]
        if answer == len(A):
            answer = -1
            break
        answer += 1
    return answer