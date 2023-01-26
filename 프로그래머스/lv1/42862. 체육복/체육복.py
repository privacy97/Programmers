def solution(n, lost, reserve):
    
    lost_del = list(set(lost)-set(reserve))
    reserve_del = list(set(reserve)-set(lost))
    
    lost_del.sort(reverse=True)
    reserve_del.sort(reverse=True)
    
    for i in range(len(reserve_del)):
        for j in range(len(lost_del)):
            if lost_del[j] == 0:
                continue
            elif reserve_del[i]+1 == lost_del[j]:
                lost_del[j] = 0
                break
            elif reserve_del[i]-1 == lost_del[j]:
                lost_del[j] = 0
                break
    
    answer = n-(len(lost_del)-lost_del.count(0))
    return answer