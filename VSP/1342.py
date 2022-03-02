from collections import Counter
string = input()

counting = Counter(string)

answer = 0
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def lucky(last):
    global answer
    cnt = 0

    for key in counting:
        
        if (counting[key] >= 1 and key == last) or (counting[key] > 1):
            break
        elif counting[key]==1:
            cnt+=1
    else:
        answer += fact(cnt)
        return
    for key in counting:
        if key != last and counting[key] > 0:
            counting[key] -= 1
            lucky(key)
            counting[key] += 1

        
lucky('')
print(answer)
    

