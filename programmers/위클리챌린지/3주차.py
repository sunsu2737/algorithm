from collections import deque
def rotation(table):
    length=len(table)

    result=[[0]*length for i in range(length)]

    for i in range(length):
        for j in range(length):
            result[i][j]=table[length-1-j][i]
    return result

def get_blocks(board,b=1):
    n=len(board)
    # print(board)
    board=[item[:] for item in board]
    dd=[(1,0),(0,1),(-1,0),(0,-1)]
    di=['d','r','u','l']
    
    blocks=[]
    # print_table(board)
    for i in range(n):
        for j in range(n):
            block=[]
            if board[i][j]==b:
                cnt=0
                next_q=deque([(i,j)])
                board[i][j]=(b+1)%2
                while next_q:
                    x,y=next_q.popleft()
                    temp=''
                    for t in range(4):
                        if 0<=x+dd[t][0]<n and 0<=y+dd[t][1]<n and board[x+dd[t][0]][y+dd[t][1]]==b:
                            cnt+=1
                            temp+=di[t]
                            board[x+dd[t][0]][y+dd[t][1]]=(b+1)%2
                            next_q.append((x+dd[t][0],y+dd[t][1]))
                    
                    block.append(temp)
                # print(block)
                # print_table(board)
                blocks.append((block,cnt+1))
            # print(blocks)
    return blocks



            


def print_table(table):
    for i in table:
        print(*i)

def delete_usedBlock(board,numbers):
    n=len(board)
    # print(board)
    b=1
    board2=[item[:] for item in board]
    dd=[(1,0),(0,1),(-1,0),(0,-1)]
    cnt=0
    # print_table(board)
    for i in range(n):
        for j in range(n):
            if board2[i][j]==b:

                next_q=deque([(i,j)])
                board2[i][j]=0
                if cnt in numbers:
                    board[i][j]=0
                while next_q:
                    x,y=next_q.popleft()

                    for t in range(4):
                        if 0<=x+dd[t][0]<n and 0<=y+dd[t][1]<n and board2[x+dd[t][0]][y+dd[t][1]]==b:

                            board2[x+dd[t][0]][y+dd[t][1]]=0
                            if cnt in numbers:
                                board[x+dd[t][0]][y+dd[t][1]]=0

                            next_q.append((x+dd[t][0],y+dd[t][1]))
                cnt+=1

                # print(block)
                # print_table(board)

            # print(blocks)




def solution(game_board, table):
    answer = 0
    board_block=get_blocks(game_board,0)
    # print(board_block)
    for _ in range(4):
        table_block=get_blocks(table)
        # print(table_block)
        used_block=[]
        for i in range(len(board_block)):
            for j in range(len(table_block)):
                if table_block and board_block[i] and  board_block[i]==table_block[j]:
                    answer+=board_block[i][1]
                    board_block[i]=False
                    table_block[j]=False
                    used_block.append(j)
        delete_usedBlock(table,used_block)
        table=rotation(table)





    return answer


game_board=[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table=[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board,table))