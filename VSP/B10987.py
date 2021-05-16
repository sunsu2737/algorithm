import sys
line=sys.stdin.readline

word=line().strip()
arr=('a','e','i','o','u')
cnt=0
for i in word:
    if i in arr:
        cnt+=1
print(cnt)