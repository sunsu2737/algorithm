def solution(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]>=1:
                    board[i+1][j+1]=min( board[i][j],board[i+1][j],board[i][j+1])+1
            except IndexError:
                break
    
    i=max(list(map(max,board)))
    
    return i*i