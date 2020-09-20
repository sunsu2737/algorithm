import sys
line=sys.stdin.readline
burger=[]
for i in range(3):
    burger.append(int(line()))
burger.sort()
juice=[]
for i in range(2):
    juice.append(int(line()))
juice.sort()
print(burger[0]+juice[0]-50)