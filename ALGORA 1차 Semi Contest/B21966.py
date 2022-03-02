n=int(input())
s=input()

if n<=25:
    print(s)
else:
    mid=s[11:-12]
    # print(mid)
    if '.' in mid:
        print(s[:9]+'......'+s[-10:])
    else:
        print(s[:11]+'...'+s[-11:])