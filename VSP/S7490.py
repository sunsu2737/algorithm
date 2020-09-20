import sys
line = sys.stdin.readline

op = [' ', '+', '-']


def get_result(string):
    st = []
    op_st = []
    for i in string:
        if '1' <= i <= '9':
            if op_st and op_st[-1] == ' ':
                st[-1] = st[-1]*10+int(i)
                op_st.pop()
            else:
                st.append(int(i))
        else:
            op_st.append(i)
    result = 0

    for i in range(len(st)):
        if i == 0:
            result += st[i]
        else:
            if op_st[i-1] == '+':
                result += st[i]
            elif op_st[i-1] == '-':
                result -= st[i]

    return result


def get_string(N, arr, string='1', level=1):
    if level == N:
        if get_result(string) == 0:
            print(string)
        return
    for i in op:
        get_string(N, arr, string+i+str(arr[level]), level+1)


T = int(line())
for _ in range(T):
    N = int(line())
    arr = [i for i in range(1, N+1)]
    get_string(N, arr)
    print()
