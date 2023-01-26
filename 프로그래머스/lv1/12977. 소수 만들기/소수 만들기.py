from itertools import combinations

# 소수 검증 함수
def primenumber(x):
    for i in range(2, x):
    	if x % i == 0:
        	return False
    return True


def solution(nums):
    
    a = list(combinations(nums, 3))
    answer = 0
    
    for i in a:
        if primenumber(sum(i)) == True:
            answer += 1
            
    return answer