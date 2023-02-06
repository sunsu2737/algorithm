import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())

temp = list(map(int, input().split()))

rect = {"A": temp[0], "B": temp[1], "C": temp[2], "D": temp[3]}


cards = defaultdict(list)

for _ in range(n):
    alpha, number = input().split()
    cards[alpha].append(int(number))
cards["A"].sort()
cards["B"].sort()
cards["C"].sort()
cards["D"].sort()


for _ in range(k):
    a, b, c, d = 0, 0, 0, 0
    if cards["A"]:
        a = (rect["A"]+cards["A"][-1]) * rect["B"] * rect["C"] * rect["D"]
    if cards["B"]:
        b = rect["A"] * (rect["B"] + cards["B"][-1]) * rect["C"] * rect["D"]
    if cards["C"]:
        c = rect["A"] * rect["B"] * (rect["C"] + cards["C"][-1]) * rect["D"]
    if cards["D"]:
        d = rect["A"] * rect["B"] * rect["C"] * (rect["D"]+cards["D"][-1])

    if max(a, b, c, d) == a:
        print("A", cards["A"][-1])
        rect["A"] += cards["A"][-1]
        cards["A"].pop()
    elif max(a, b, c, d) == b:
        print("B", cards["B"][-1])
        rect["B"] += cards["B"][-1]
        cards["B"].pop()
    elif max(a, b, c, d) == c:
        print("C", cards["C"][-1])
        rect["C"] += cards["C"][-1]
        cards["C"].pop()
    elif max(a, b, c, d) == d:
        print("D", cards["D"][-1])
        rect["D"] += cards["D"][-1]
        cards["D"].pop()
