import sys
line=sys.stdin.readline

price,money=10,20

money=10**money

if price%money<money*0.5:
    print(price-price%money)
else:
    print(price-price%money+money)