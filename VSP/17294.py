
def solve():
    arr=list(map(int,list(input())))
    if len(arr)==1:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
        return


    temp=arr[1]-arr[0]


    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]!=temp:
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            return
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

solve()