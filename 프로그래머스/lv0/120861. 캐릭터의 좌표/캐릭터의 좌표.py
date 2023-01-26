def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        temp0 = board[0]//2
        temp1 = board[1]//2
        if i == 'up':
            if answer[1] == temp1:
                pass
            else:
                answer[1] += 1
        elif i == 'down':
            if answer[1] == -temp1:
                pass
            else:
                answer[1] -= 1
        elif i == 'left':
            if answer[0] == -temp0:
                pass
            else:
                answer[0] -= 1
        else:
            if answer[0] == temp0:
                pass
            else:
                answer[0] += 1
    return answer