from itertools import combinations

def solution(numbers):
    '''
    numbers.sort()
    answer = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    '''
    answer = float("-inf")
    for i in list(combinations(numbers, 2)):
        if answer < i[0] * i[1]:
            answer = i[0] * i[1]
        
    return answer