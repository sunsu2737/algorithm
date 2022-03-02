num_list = list(map(int,input().split()))

num_list.sort()

a,b,c = num_list

answer = a

b, c = b - a, c - a

answer += b // 3 + c // 3

b, c = b % 3, c % 3

if (b==0 or c==0) and (b!=0 or c!=0):
    answer+=1
else:
    answer+=max(b,c)

print(answer)

