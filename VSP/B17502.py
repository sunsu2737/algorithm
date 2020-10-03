import sys
line = sys.stdin.readline

n=int(line())

word=list(line().strip())

for i,w in enumerate(word):
    if w=='?':
        if word[n-1-i]=='?':
            word[i]='a'
            word[n-1-i]='a'
        else:
            word[i]=word[n-1-i]
print(''.join(word))