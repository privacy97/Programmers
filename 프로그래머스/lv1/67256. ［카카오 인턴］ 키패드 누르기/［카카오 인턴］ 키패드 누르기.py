def solution(numbers, hand):
    
    pad_dic = {
        1:[0, 0], 2:[0, 1], 3:[0, 2],
        4:[1, 0], 5:[1, 1], 6:[1, 2],
        7:[2, 0], 8:[2, 1], 9:[2, 2],
        '*':[3, 0], 0:[3, 1], '#':[3, 2]
    }
    
    left = pad_dic['#']
    right = pad_dic['*']
    answer = ''
    
    for i in range(len(numbers)):
        now = pad_dic[numbers[i]]
        
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left = now
            answer += 'L'
            
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right = now
            answer += 'R'
            
        else:
            left_dt = abs(left[0] - now[0]) + abs(left[1] - now[1])
            right_dt = abs(right[0] - now[0]) + abs(right[1] - now[1])
            
            if left_dt < right_dt:
                left = now
                answer += 'L'
            elif left_dt > right_dt:
                right = now
                answer += 'R'
            else:
                if hand == 'left':
                    left = now
                    answer += 'L'
                elif hand == 'right':
                    right = now
                    answer += 'R'

    return answer