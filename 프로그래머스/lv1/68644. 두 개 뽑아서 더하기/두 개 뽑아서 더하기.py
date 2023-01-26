from itertools import combinations

def solution(numbers):
    
    num_list = list(combinations(numbers, 2))
    answer = []
    
    for i in num_list:
        answer.append(sum(i))
    
    answer = sorted(list(set(answer)))
    
    return answer