from itertools import combinations

def solution(number):
    
    num_list = list(combinations(number, 3))
    answer = 0
    
    for i in num_list:
        if sum(i) == 0:
            answer += 1
            
    return answer

n = 5
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            print(i, j, k)
            


