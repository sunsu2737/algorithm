


def solution(order):
    answer = 0
    belt = [i for i in range(len(order),0,-1)]
    sub = []
    count = 0
    flag = True
    for i in order:
        while True:
            if belt and belt[-1] < i:
                sub.append(belt.pop())
            elif belt and belt[-1] == i:
                belt.pop()
                count+=1
                break
            else:

                if sub and sub[-1] == i:
                    sub.pop()
                    count+=1
                    break
                else:
                    flag=False
                    break
        if not flag:
            break

    return count