import math

def solution(n):
    count = 0
    while True:
        count += 1
        if (count*6)%n == 0:
            break
    return count