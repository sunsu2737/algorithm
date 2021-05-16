import sys
line=sys.stdin.readline

number1=int(line())
operator=line().strip()
number2=int(line())

if operator=='+':
    print(number1+number2)

if operator=='*':
    print(number1*number2)