def turn(key):
    new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[i][j] = key[len(key)-j-1][i]
    return new_key

def insert_key(key,door,i,j):
    key_size=len(key)
    for x in range(i,i+key_size):
        for y in range(j,j+key_size):
            door[x][y]+=key[x-i][y-j]

def del_key(key,door,i,j):
    key_size=len(key)
    for x in range(i,i+key_size):
        for y in range(j,j+key_size):
            door[x][y]-=key[x-i][y-j]

def check(size,door,i,j):
    flag=0
    for x in range(size,size*2):
        for y in range(size,size*2):
            if door[x][y]!=1:
                flag=1
                break
            else:
                flag=0
        if flag==1:
            break
    if flag==0:
        return True    

def solution(key, lock):

    size=len(lock)
    key_size=len(key)
    door=[[0 for _ in range(size*3)]for _ in range(size*3)]
    for i in range(size,size*2):
        for j in range(size,size*2):
            door[i][j]=lock[i-size][j-size]

    for _ in range(3):
        for i in range(size-key_size,size*2):
            for j in range(size-key_size,size*2):
                insert_key(key,door,i,j)
                if check(size,door,i,j):
                    return True

                del_key(key,door,i,j)

        key=turn(key)
    return False