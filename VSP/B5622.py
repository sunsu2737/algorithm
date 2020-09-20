import sys
line = sys.stdin.readline

string = line()

number_table = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6, "MNO": 7, "PQRS": 8, "TUV":9,"WXYZ": 10}
cnt=0
for i in string:
    for j,k in number_table.items():
        if i in j:
            cnt+=k
            break
print(cnt)