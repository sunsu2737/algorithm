import sys
from collections import deque
line = sys.stdin.readline

N, M = map(int, line().split())



if N%3==0 or N%3==1:
    s=N//3+1
    e=N-N//3
    if s<=M and M<=e:
        print('YES')
    else:
        print('NO')
elif N%3==2:
    s=N//3+1
    e=N-N//3-1
    if s<=M and M<=e:
        print('YES')
    else:
        print('NO')


# pizza = deque()
# for _ in range(N):
#     pizza.append(tuple(line().split()))

# if M == N == 1:
#     print('YES')


# elif M > N//2 and M-N//2 > N//2:
#     print('NO')
# elif M <= N//2 and N//2-M > N//2:
#     print('NO')
# else:
#     print('YES')

# flag = 1
# if N==1 and M==1:
#     print('YES')
#     exit()
# while True:
#     if N == M :
#         flag = 0
#         break

#     N -= 1
#     if N == 1 and M == 1:
#         break
#     if M==1:
#         flag = 0
#         break
#     N -= 1

#     M -= 1
#     if N == 1 and M == 1:
#         break
#     if M > N//2:
#         N -= 1
#         M -= 1
#     else:
#         N -= 1
#     if N == 1 and M == 1:
#         break
# if flag == 1:
#     print('YES')
# else:
#     print('NO')

# answer=pizza[M-1][1]

# while True:
#     if len(pizza)==1:
#         break
#     pizza.pop()
#     if len(pizza)==1:
#         break
#     pizza.popleft()
#     if len(pizza)==1:
#         break
#     if N//2<M:
#         pizza.popleft()
#         N+=1
#     else:
#         pizza.pop()
#         N-=1
# if pizza[0][1]==answer:
#     print('YES')
# else:
#     print('NO')
