from collections import Counter
T = int(input())

input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))

A_sum = []
B_sum = []


for i in A:
    if A_sum:
        A_sum.append(A_sum[-1]+i)
    else:
        A_sum.append(i)

for i in B:
    if B_sum:
        B_sum.append(B_sum[-1]+i)
    else:
        B_sum.append(i)

B_list = []
A_list = []
# print(A_sum)
# print(B_sum)
for i in range(len(B_sum)):
    B_list.append(B_sum[i])
    for j in range(i):
        B_list.append(B_sum[i]-B_sum[j])
for i in range(len(A_sum)):
    A_list.append(A_sum[i])
    for j in range(i):
        A_list.append(A_sum[i]-A_sum[j])

B_list = sorted(list(Counter(B_list).items()))


answer = 0
# print(A_list)
# print(B_list)
for i in A_list:
    start = 0
    end = len(B_list)-1
    t = i

    while start <= end:
        mid = (start+end)//2
        if B_list[mid][0]+t == T:
            answer += B_list[mid][1]
            break
        elif B_list[mid][0]+t > T:
            end = mid-1
        else:
            start = mid+1
print(answer)
