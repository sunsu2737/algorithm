import copy
def solution(grid):
    answer = []
    r=len(grid)
    c=len(grid[0])

    able_path=[[[0,0,0,0] for i in range(c)]for n in range(r)]


                
    able_path2=copy.deepcopy(able_path)

    direct=[(0,1),(1,0),(0,-1),(-1,0)]



    for i in range(r):
        for j in range(c):
            for k in range(4):
                bim=(i,j,k)
                cnt=0
                # print("start->",bim,grid[i][j])
                # print(able_path)
                
                if able_path[i][j][k]==0:
                    cnt+=1
                    able_path[i][j][k]=1

                    if grid[i][j]=='S':
                        next_bim=((i+direct[k][0])%r,(j+direct[k][1])%c,k)
                    elif grid[i][j]=='R':
                        next_bim=((i+direct[(k+1)%4][0])%r,(j+direct[(k+1)%4][1])%c,(k+1)%4)
                    else:
                        next_bim=((i+direct[(k-1)%4][0])%r,(j+direct[(k-1)%4][1])%c,(k-1)%4)

                    
                    
                    while next_bim!=bim :
                        cnt+=1

                        x,y,z=next_bim
                        able_path[x][y][z]=1
                        # print(next_bim,grid[x][y],end='->')
                        if grid[x][y]=='S':
                            next_bim=((x+direct[z][0])%r,(y+direct[z][1])%c,z)
                        elif grid[x][y]=='R':
                            next_bim=((x+direct[(z+1)%4][0])%r,(y+direct[(z+1)%4][1])%c,(z+1)%4)
                        else:
                            next_bim=((x+direct[(z-1)%4][0])%r,(y+direct[(z-1)%4][1])%c,(z-1)%4)
                        # print(next_bim)

                    answer.append(cnt)



    answer.sort()
    return answer


print(solution(["SL","LR"]))