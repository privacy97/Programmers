def solution(n):
    return sum(map(int, list(reversed(list(str(n))))))