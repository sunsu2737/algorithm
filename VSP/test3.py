from collections import deque


def solution(board, r, c):
    curser = [r, c]

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    first_find = (0, 3)
    answer = 0
    open_card = [0, 0, 0]
    while True:
        # for i in board:
        #     print(i)
        # print(open_card, curser, answer)
        # print()
        if open_card[2] == 0:
            next_curser = [0, 0]
            check = [[0]*4 for _ in range(4)]
            check[r][c] = 1
            next = deque()
            next.append(curser)
            while next:
                r, c = next.pop()
                if board[r][c] != 0:
                    next_curser = [r, c]
                    open_card = [r, c, board[r][c]]
                    board[r][c] = 0
                    break
                if board[r][0] != 0 and check[r][0] == 0:
                    next_curser = [r, 0]
                    open_card = [r, 0, board[r][0]]
                    board[r][0] = 0
                    break
                if board[0][c] != 0 and check[0][c] == 0:
                    next_curser = [0, c]
                    open_card = [0, c, board[0][c]]
                    board[0][c] = 0
                    break
                if board[r][3] != 0 and check[r][3] == 0:
                    next_curser = [r, 3]
                    open_card = [r, 3, board[r][3]]
                    board[r][3] = 0
                    break
                if board[3][c] != 0 and check[3][c] == 0:
                    next_curser = [3, c]
                    open_card = [3, c, board[3][c]]
                    board[3][c] = 0
                    break
                flag = 0
                for i in first_find:
                    for j in range(4):
                        if board[i][j] != 0:
                            next_curser = [i, j]
                            open_card = [i, j, board[i][j]]
                            board[i][j] = 0
                            flag = 1
                            break
                        if board[j][i] != 0:
                            next_curser = [j, i]
                            open_card = [j, i, board[j][i]]
                            board[j][i] = 0
                            flag = 1
                            break

                    if flag == 1:
                        break
                if flag == 1:
                    break
                for j in range(4):
                    if board[r][j] != 0:
                        next_curser = [r, j]
                        open_card = [r, j, board[r][j]]
                        board[r][j] = 0
                        flag = 1
                        break
                    if board[j][c] != 0:
                        next_curser = [j, c]
                        open_card = [j, c, board[j][c]]
                        board[j][c] = 0
                        flag = 1
                        break

                if flag == 1:
                    break
                for dr, dc in d:
                    if 0 <= r+dr <= 3 and 0 <= c+dc <= 3 and check[r+dr][c+dc] == 0:
                        next.appendleft([r+dr, c+dc])
                        check[r+dr][c+dc] = 1
            if open_card[2] == 0:
                break
            if next_curser[0] == curser[0] and next_curser[1] == curser[1]:
                pass
            elif next_curser[0] == curser[0] or next_curser[1] == curser[1]:
                answer += 1
                curser[0] = next_curser[0]
                curser[1] = next_curser[1]
            elif next_curser[0] in [0, 3] or next_curser[1] in [0, 3]:
                answer += 2
                curser[0] = next_curser[0]
                curser[1] = next_curser[1]

            else:
                answer += abs(next_curser[0]-curser[0]) + \
                    abs(next_curser[1]-curser[1])
                curser[0] = next_curser[0]
                curser[1] = next_curser[1]
            answer += 1
        else:
            next_curser = [0, 0]
            check = [[0]*4 for _ in range(4)]
            check[r][c] = 1
            next = deque()
            next.append(curser)
            while next:
                r, c = next.pop()
                if board[r][c] == open_card[2]:

                    next_curser = [r, c]
                    open_card = [0, 0, 0]
                    board[r][c] = 0
                    break
                for dr, dc in d:
                    if 0 <= r+dr <= 3 and 0 <= c+dc <= 3 and check[r+dr][c+dc] == 0:
                        next.appendleft([r+dr, c+dc])
                        check[r+dr][c+dc] = 1

            if next_curser[0] == curser[0] or next_curser[1] == curser[1]:
                answer += 1
                curser[0] = next_curser[0]
                curser[1] = next_curser[1]
            elif next_curser[0] in [0, 3] or next_curser[1] in [0, 3]:
                answer += 2
                curser[0] = next_curser[0]
                curser[1] = next_curser[1]

            else:
                answer += abs(next_curser[0]-curser[0]) + \
                    abs(next_curser[1]-curser[1])
                curser[0] = next_curser[0]
                curser[1] = next_curser[1]
            answer += 1

    return answer


print(solution([[1, 1, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [0, 0, 0, 0]], 1, 0))
