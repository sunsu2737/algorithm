
n = int(input())
arr = list(map(int, list(input())))
goal = list(map(int, list(input())))
answer = 999999999
# print(arr)

def solve(bulb,cnt):
    global answer
    for deep in range(1,n):


        if deep == n-1:
            if bulb[deep-1] != goal[deep-1]:
                bulb[deep-1] = (bulb[deep-1] + 1) % 2
                bulb[deep] = (bulb[deep] + 1) % 2
                cnt+=1

        else:
            if bulb[deep-1] != goal[deep-1]:
                bulb[deep-1] = (bulb[deep-1] + 1) % 2
                bulb[deep] = (bulb[deep] + 1) % 2
                bulb[deep+1] = (bulb[deep+1] + 1) % 2
                cnt+=1

    for i in range(n):
        if bulb[i] != goal[i]:
            break
    else:
        answer = min(answer, cnt)



arr2 = arr[::]
arr2[0] = (arr2[0]+1) % 2
arr2[1] = (arr2[1]+1) % 2
solve(arr,0)
solve(arr2,1)
if answer==999999999:
    print(-1)
else:
    print(answer)
