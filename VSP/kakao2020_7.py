from collections import deque

def solution(board):
    N=len(board)
    check=set()
    check.add((0,0,0,1,0))

    next=deque()
    next.append(((0,0,0,1,0,0)))
    while next:
        x1,y1,x2,y2,st,answer=next.popleft()

        if (x1==N-1 and y1==N-1) or (x2==N-1 and y2==N-1):
            return answer

        if 0<=x1+1<N and 0<=y1<N and 0<=x2+1<N and 0<=y2<N and board[x1+1][y1]==0 and board[x2+1][y2]==0 and (x1+1,y1+1,x2,y2,st) not in check:
            next.append((x1+1,y1,x2+1,y2,st,answer+1))
            check.add((x1+1,y1,x2+1,y2,st))

        if 0<=x1<N and 0<=y1+1<N and 0<=x2<N and 0<=y2+1<N and board[x1][y1+1]==0 and board[x2][y2+1]==0 and (x1,y1+1,x2,y2+1,st)not in check:
            next.append((x1,y1+1,x2,y2+1,st,answer+1))
            check.add((x1,y1+1,x2,y2+1,st))

        if 0<=x1-1<N and 0<=y1<N and 0<=x2-1<N and 0<=y2<N and board[x1-1][y1]==0 and board[x2-1][y2]==0 and  (x1-1,y1,x2-1,y2,st)not in check:
            next.append((x1-1,y1,x2-1,y2,st,answer+1))
            check.add((x1-1,y1,x2-1,y2,st))

        if 0<=x1<N and 0<=y1-1<N and 0<=x2<N and 0<=y2-1<N and board[x1][y1-1]==0 and board[x2][y2-1]==0 and  (x1,y1-1,x2,y2-1,st)not in check:
            next.append((x1,y1-1,x2,y2-1,st,answer+1))
            check.add((x1,y1-1,x2,y2-1,st))


        if st==0 and 0<=x1+1<N and board[x1+1][y1]==0 and board[x2+1][y2]==0:
            if (x1+1,y2,x2,y2,1) not in check:
                next.append((x1+1,y2,x2,y2,1,answer+1))
                check.add((x1+1,y2,x2,y2,1))
            if (x1,y1,x2+1,y1,1) not in check:
                next.append((x1,y1,x2+1,y1,1,answer+1))
                check.add((x1,y1,x2+1,y1,1))
        if st==0 and 0<=x1-1<N and board[x1-1][y1]==0 and board[x2-1][y2]==0:
            if (x1-1,y2,x2,y2,1) not in check:
                next.append((x1-1,y2,x2,y2,1,answer+1))
                check.add((x1-1,y2,x2,y2,1))
            if (x1,y1,x2-1,y1,1) not in check:
                next.append((x1,y1,x2-1,y1,1,answer+1))
                check.add((x1,y1,x2-1,y1,1))
        if st==1 and 0<=y1+1<N and board[x1][y1+1]==0 and board[x2][y2+1]==0:
            if (x2,y1+1,x2,y2,0) not in check:
                next.append((x2,y1+1,x2,y2,0,answer+1))
                check.add((x2,y1+1,x2,y2,0))
            if (x1,y1,x1,y2+1,0) not in check:
                next.append((x1,y1,x1,y2+1,0,answer+1))
                check.add((x1,y1,x1,y2+1,0))
        if st==1 and 0<=y1-1<N and board[x1][y1-1]==0 and board[x2][y2-1]==0:
            if (x2,y1-1,x2,y2,0) not in check:
                next.append((x2,y1-1,x2,y2,0,answer+1))
                check.add((x2,y1-1,x2,y2,0))
            if (x1,y1,x1,y2-1,0) not in check:
                next.append((x1,y1,x1,y2-1,0,answer+1))
                check.add((x1,y1,x1,y2-1,0))
    return answer

print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))