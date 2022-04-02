n = int(input())

if n%10>0:
    print(-1)
else:
    button = [300,60,10]

    for b in button:
        print(n//b,end=' ')
        n = n%b