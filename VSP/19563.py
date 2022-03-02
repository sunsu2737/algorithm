a,b,c=map(abs,map(int,input().split()))

print('YES' if c-a-b>=0 and (c-a-b)%2==0 else 'NO')