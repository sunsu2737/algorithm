import sys
line=sys.stdin.readline

N=int(line())
string_list=set()
for _ in range(N):
    string=line().strip()
    string_len=len(string)
    string_list.add((string_len,string))
string_list=list(string_list)
string_list.sort()
for i in string_list:
    print(i[1])

