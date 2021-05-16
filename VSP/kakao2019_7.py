
#TODO:다시풀어보기(틀렸음)
possible = [((1, 0), (1, 1), (1, 2)), ((1, 0), (2, 0), (2, -1)), ((1, 0),
                                                                  (2, 0), (2, 1)), ((1, 0), (1, -1), (1, -2)), ((1, 0), (1, -1), (1, 1))]


def check(board, x, y):
    flag = 0
    number = board[x][y]
    for block in possible:
        for b in block:
            if x+b[0] < 0 or x+b[0] >= len(board) or y+b[1] < 0 or y+b[1] >= len(board) or board[x+b[0]][y+b[1]] != number:
                flag = 1
                break
            elif board[x+b[0]][y+b[1]] == number:
                flag = 0
        if flag == 0:
            for b in block:
                board[x+b[0]][y+b[1]] = 0
                board[x][y] = 0
            return True
    return False


def del_line(board, x, y):

    number = board[x][y]

    if 0 <= y+2 < len(board) and board[x][y+1] == number and board[x][y+2] == number:
        for i in range(x, len(board)):
            board[i][y] = 0
            board[i][y+1] = 0
            board[i][y+2] = 0
    elif 0 <= y+1 < len(board) and board[x][y+1] == number:
        for i in range(x, len(board)):
            board[i][y] = 0
            board[i][y+1] = 0
    else:
        if 0 <= x+1 < len(board) and 0 <= y+1 < len(board) and board[x+1][y+1] == number:
            for i in range(x, len(board)):
                board[i][y] = 0
                board[i][y+1] = 0
        elif 0 <= x+1 < len(board) and 0 <= y-1 < len(board) and board[x+1][y-1] == number:
            for i in range(x, len(board)):
                board[i][y] = 0
                board[i][y-1] = 0
        else:
            for i in range(x,len(board)):
                board[i][y]=0

def print_board(board):
    for i in board:
        print(*i)
    print()


def solution(board):
    answer = 0
    #print_board(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                if check(board, i, j):
                    answer += 1
                    #print_board(board)
                else:
                    del_line(board, i, j)
                    #print_board(board)
    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
      0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
