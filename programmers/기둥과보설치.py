def check(wall):
    for x, y, what in wall:
        if what == 0:
            if y == 0 or (x, y-1, 0) in wall or (x-1, y, 1) in wall or (x, y, 1) in wall:
                continue
            else:
                return True
        if what == 1:
            if (x, y-1, 0) in wall or (x+1, y-1,0) in wall or ((x-1, y, 1) in wall and (x+1, y, 1) in wall):
                continue
            else:
                return True
    return False


def solution(n, build_frame):
    wall = set()
    for x, y, what, how in build_frame:
        if how == 1:
            wall.add((x, y, what))
            if check(wall):
                wall.remove((x, y, what))

        else:
            wall.remove((x, y, what))
            if check(wall):
                wall.add((x, y, what))
    answer = []
    for ans in wall:
        answer.append(list(ans))
    answer.sort()

    return answer