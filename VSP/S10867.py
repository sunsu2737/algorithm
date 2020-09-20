import sys
line = sys.stdin.readline

N = line()

number_list = sorted(list(set(map(int, line().split()))))

print(*number_list)
