def solution(lottos, win_nums):
    
    cor_cnt = 0
    zero_cnt = 0
    
    for i in lottos:
        if i == 0:
            zero_cnt += 1
        else:
            if i in win_nums:
                cor_cnt += 1
                
    high = 7-(zero_cnt+cor_cnt)
    low = 7-(cor_cnt)
    
    if low == 7:
        low = 6
    if high == 7:
        high = 6

    answer = [high, low]
    
    return answer