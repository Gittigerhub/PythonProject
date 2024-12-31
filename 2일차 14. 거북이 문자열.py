"""
        입력 대화상자를 이용해서 문자열을 입력받아
        한글자씩 분리하여 임의의 크기 및 색상, 위치로 출력하는 프로그램
"""

import turtle
import random
from tkinter.simpledialog import *      # 윈도우 라이브러리 (대화상자 일부분) / 특정한 패키지 안에 내용을 가져올때 from

inStr = ""                                              # 입력받은 문자열을 저장할 변수
swidth, sheight = 300, 300                              #  윈도우 크기

tX, tY, txtSize = [0] * 3                               # 난수로 생성할 위치, 글자 크기를 저장할 변수

turtle.title("거북이 문자열 출력")
turtle.shape("turtle")
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()                                          # 선그리기 해제

# askstring("창제목", "문자열") => 문자열 입력 대화상자
inStr = askstring("문자열 입력", "문자열을 입력하세요.")

for ch in inStr:                                        # 문자열을 한글자씩 분리해서 반복
    # 작업에 필요한 값들을 난수로 완성
    tX = random.randrange(int(-swidth/2), int(swidth/2))
    tY = random.randrange(int(-sheight / 2), int(sheight / 2))
    # 한행에 여러 문장을 표현할 때 ;을 사용한다.
    r = random.random(); g = random.random(); b = random.random()
    txtSize = random.randrange(10, 50)

    turtle.goto(tX, tY)                                 # 출력할 위치로 거북이를 이동
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=("Arial", txtSize, 'bold'))   # 해당 문자를 출력

turtle.done()