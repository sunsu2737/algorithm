import sys
line = sys.stdin.readline

N=line()
balls=[]
for i in sys.stdin:
    a=list(map(int,i.split()))
    balls.append(a)

dist=[]


for i in range(len(balls)-1):
    ball=[]
    for j in range(len(balls[i])):
        speed=set()
        for k in range(len(balls[i+1])):
            speed.add(balls[i+1][k]-balls[i][j])
        ball.append(speed)
    if dist:
        # print(ball)
        for idx,a in enumerate(dist):
            y=set()
            for b in ball:
                m=a&b
                y=y|m
            dist[idx]=y
    else:
        dist=ball
    flag=0
    for idx,j in enumerate(dist):
        if len(j)!=1:
            flag=1
            break
        
        

    if flag==0:
        break
        # print(dist)
answer=list(zip(balls[0],dist))
answer.sort()

for i in range(len(balls[0])):
    print(answer[i][0],answer[i][1].pop())

# print(dist)
# candidate=dist[0]
# for i in range(1,len(dist)):
#     for idx,j in enumerate(candidate):
#         y=set()
#         for k in dist[i]:
#             m=j&k
#             # print(m)
#             y=y.union(m)
#         candidate[idx]=y
# # print(candidate)
# candidate=list(zip(balls[0],candidate))
# candidate.sort()
# for i in range(len(balls[0])):
#     print(candidate[i][0],candidate[i][1].pop())

