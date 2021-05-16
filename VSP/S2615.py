board=[]
for i in range(19):
    board.append(input().split())


for i in range(19):
    for j in range(19):
        if board[j][i]=='1':
            try:
                if board[j+1][i]=='1' and board[j+2][i]=='1' and board[j+3][i]=='1' and board[j+4][i]=='1' and (j+5>18 or board[j+5][i]!='1') and (j-1<0 or board[j-1][i]!='1'):
                    print(1)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
            try:
                if board[j][i+1]=='1' and board[j][i+2]=='1' and board[j][i+3]=='1' and board[j][i+4]=='1' and (i+5>18 or board[j][i+5]!='1') and (i-1<0 or board[j][i-1]!='1'):
                    print(1)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
            try:
                if board[j+1][i+1]=='1' and board[j+2][i+2]=='1' and board[j+3][i+3]=='1' and board[j+4][i+4]=='1'  and (j+5>18 or i+5>18 or  board[j+5][i+5]!='1') and (j-1<0 or i-1<0 or board[j-1][i-1]!='1'):
                    print(1)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
            try:
                if board[j-1][i+1]=='1' and board[j-2][i+2]=='1' and board[j-3][i+3]=='1' and board[j-4][i+4]=='1'  and (j-5<0 or i+5>18 or  board[j-5][i+5]!='1') and (j+1>18 or i-1<0 or board[j+1][i-1]!='1'):
                    print(1)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
        elif board[j][i]=='2':
            try:
                if board[j+1][i]=='2' and board[j+2][i]=='2' and board[j+3][i]=='2' and board[j+4][i]=='2' and (j+5>18 or board[j+5][i]!='2') and (j-1<0 or board[j-1][i]!='2'):
                    print(2)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
            try:
                if board[j][i+1]=='2' and board[j][i+2]=='2' and board[j][i+3]=='2' and board[j][i+4]=='2' and (i+5>18 or board[j][i+5]!='2') and (i-1<0 or board[j][i-1]!='2'):
                    print(2)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
            try:
                if board[j+1][i+1]=='2' and board[j+2][i+2]=='2' and board[j+3][i+3]=='2' and board[j+4][i+4]=='2' and (j+5>18 or i+5>18 or  board[j+5][i+5]!='2') and (j-1<0 or i-1<0 or board[j-1][i-1]!='2'):
                    print(2)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass
            try:
                if board[j-1][i+1]=='2' and board[j-2][i+2]=='2' and board[j-3][i+3]=='2' and board[j-4][i+4]=='2' and (j-5<0 or i+5>18 or  board[j-5][i+5]!='2') and (j+1>18 or i-1<0 or board[j+1][i-1]!='2'):
                    print(2)
                    print(j+1,i+1)
                    exit(0)
            except IndexError:
                pass

print(0)