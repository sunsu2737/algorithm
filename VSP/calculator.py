# 모듈 import
from tkinter import *
import parser
from math import factorial

# 상수 정의
LOC = 0
TOGGLE = True
WIDTH = 5
HEIGHT = 2
# GUI 정의
root = Tk()
root.title('Calculator')

# 버튼 텍스트 정의
buttons = ["1", "2", "3", "+", "pi", "<-", "4", "5", "6", "-", "%",
           "x!", "7", "8", "9", "*", "(", ")", "AC", "0", ".", "/", "exp", "^2"]

# 계산기 디스플레이 생성
display = Entry(root, width=WIDTH*2)
display.grid(row=2, columnspan=6, sticky=N+E+W+S)

# 버튼 위치 변수 정의
count = 0
row = 2
col = 0

# 토글 검사 함수
def check_flag():
    global LOC
    global TOGGLE
    if not TOGGLE:
        display.delete(0, END)
        TOGGLE = True
        LOC = 0

# 소수점 아래가 0인지 확인하는 함수
def to_int():
    string = display.get()
    # 결과의 소수점 아래가 0이면 정수로 변환
    try:
        assert string[-1] != '.'
        result = float(string)
        if result % 1 == 0:
            result = int(result)
        display.delete(0, END)
        display.insert(0, result)
    except:
        pass

# 숫자 버튼 처리 함수
def get_variables(num):
    # 숫자 버튼을 누르면 현재 위치에 숫자를 추가한다.
    global LOC
    global TOGGLE
    check_flag()
    if TOGGLE:
        display.insert(LOC, num)
        LOC += 1

# 연산자 버튼 처리함수
def get_operation(operator):
    global LOC
    global TOGGLE
    string = display.get()
    try:
        if operator == 'AC': # AC 버튼을 누르면 모든 내용을 지운다.
            check_flag()
            display.delete(0, END)
            LOC = 0
        elif operator == '<-': # <- 버튼을 누르면 이전에 입력한 내용을 지운다.
            if TOGGLE:
                if string[-1]=='i':
                    display.delete(LOC-1, LOC)
                    LOC -= 1
                display.delete(LOC-1, LOC)
                LOC -= 1
                if LOC < 0:
                    LOC = 0
            else:
                display.delete(0, END)
                TOGGLE = True
                LOC = 0
        elif operator == 'exp': # exp 버튼을 누르면 숫자의 지수를 계산한다.
            result = parser.expr("2.71828**"+string).compile()
            result = eval(result)
            display.delete(0, END)
            display.insert(0, result)
            LOC += len(str(result))
            TOGGLE = False
        elif operator == '%': # % 버튼을 누르면 현재 숫자의 백분율을 계산한다.
            assert '*' in string
            assert 2 == len(string.split('*'))
            result = parser.expr(string+"/100").compile()
            result = eval(result)
            display.delete(0, END)
            display.insert(0, result)
            LOC += len(str(result))
            TOGGLE = False
        elif operator == 'x!': # x! 버튼을 누르면 현재 숫자의 팩토리얼을 계산한다.
            assert string.isdigit()
            result = factorial(int(string))
            display.delete(0, END)
            display.insert(0, result)
            LOC += len(str(result))
            TOGGLE = False
        elif operator == 'pi': # pi가 들어갈수 있는 자리일때만 pi를 추가한다.
            check_flag()
            if not string or (not string[-1].isdigit() and string[-1] != '!'):
                display.insert(LOC, operator)

                LOC += len(operator)
        else: # 연산자를 누르면 현재 위치에 연산자를 추가한다.
            display.insert(LOC, operator)
            TOGGLE = True
            LOC += len(operator)

    except:
        TOGGLE = False
        display.delete(0, END)
        display.insert(LOC, "Error")
        LOC = 5
    to_int()

# 계산 함수
def calculate():
    global TOGGLE
    TOGGLE = False
    try:
        # 디스플레이에 표시된 내용을 연산한다.
        global LOC
        equation = display.get()
        equation = equation.replace('pi', '3.141592653589793')
        equation = equation.replace('^', '**')

        result = parser.expr(equation).compile()
        result = eval(result)
        display.delete(0, END)
        display.insert(0, result)
        LOC += len(str(result))
    except:
        display.delete(0, END)
        display.insert(LOC, "Error")
        LOC = 5
    to_int()

# 버튼 생성
for i in buttons:
    if count % 6 == 0:
        row += 1
        col = 0
    if i.isdigit():
        Button(root, text=i, command=lambda x=i: get_variables(x), width=WIDTH, height=HEIGHT).grid(
            row=row, column=col, sticky=N+E+W+S)
    else:
        Button(root, text=i, command=lambda x=i: get_operation(x), width=WIDTH, height=HEIGHT).grid(
            row=row, column=col, sticky=N+E+W+S)
    col += 1
    count += 1
# 계산 버튼 생성
Button(root, text="=", command=lambda: calculate(), width=WIDTH, height=HEIGHT).grid(
    row=7, columnspan=6, sticky=N+S+E+W)

root.mainloop()
