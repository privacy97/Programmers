'''
# 이전에 풀었던 0단계 74번 소인수분해 코드
def function(n):
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

def solution(a, b):
    a = function(a)
    b = function(b)
    for i in a:
        while True:
            try:
                b.remove(i)
            except:
                break
    answer = 1
    for i in set(b):
        if not(i == 2 or i == 5):
            answer = 2
            break
    return answer
'''
from math import gcd

def solution(a, b):
    # 하단 힌트보고 푼 것
    b //= gcd(a,b)
    answer = 1
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    if b != 1:
        answer = 2
    return answer