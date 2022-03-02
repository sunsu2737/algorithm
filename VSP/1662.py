n = input()


def unzip(i):
    string = ''
    
    while i<len(n):
        # print(n[i])
        if n[i] == '(':
            s,i=unzip(i+1)
            string = len(string[:len(string)-1])+int(string[-1])*s
            return (string,i)
        if n[i] ==')':
            return (len(string),i+1)
        string+=n[i]
        i+=1
    return (len(string),i)
answer = 0
i = 0
while i < len(n):
    l, i = unzip(i)
    # print(l)
    answer += l
print(answer)
