def solution(s):
    cnt = ['', 0, 0]
    start = 0
    answer = []
    
    for i in range(len(s)):
        if cnt[1] == cnt[2]:
            answer.append(s[start:i])
            cnt = [s[i], 1, 0]
            start = i
        elif cnt[0] == s[i]:
            cnt[1] += 1 
        else:
            cnt[2] += 1 

    return len(answer)