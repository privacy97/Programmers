def solution(nums):
    
    # N/2
    n = len(nums) / 2
    
    # 중복제거
    nums = len(set(nums))
    
    # 둘 중 작은거~
    answer = min(n, nums)
    
    return answer