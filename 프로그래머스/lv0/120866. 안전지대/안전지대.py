def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 2
                if i-1 >= 0 and j-1 >= 0:
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                if i-1 >= 0:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                if i-1 >= 0 and j+1 < n:
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2
                if j-1 >= 0:
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                if j+1 < n:
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2
                if i+1 < n and j+1 < n:
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2
                if i+1 < n:
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                if i+1 < n and j-1 >= 0:
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2
    answer = 0
    for i in range(n):
        answer += board[i].count(0)
    return answer