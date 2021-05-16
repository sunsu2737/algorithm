import sys
line = sys.stdin.readline

n = int(line())
m = n
people = [i for i in range(n+1)]

person = 1
for i in range(1, n):
    turn = (i**3)%m
    if turn==0:
        turn=m
    state = 0
    # print(people)
    while True:

        state += 1
        if state == turn:
            # print(turn)
            people[person] = 0
            person += 1
            if person > n:
                person = 1
            while people[person] == 0:
                person += 1
                if person > n:
                    person = 1
            break

        person += 1
        if person > n:
            person = 1
        while people[person] == 0:
            person += 1
            if person > n:
                person = 1
    m -= 1
# print(people)
print(sum(people))
