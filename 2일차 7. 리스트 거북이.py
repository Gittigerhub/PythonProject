"""
        거북이를 이용해서 중앙에서 지정된 위치로 선을 그리는 프로그램
        100마리 거북이 도형, 위치, 색상, 선두께를 난수로 생성을 해서
        리스트에 저장 후, 저장된 리스트 정보를 이용해서 화면에 그린다.
"""

import turtle
import random

# 난수 값을 저장할 변수들 선언
myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList = []              # 도형을 저장할 리스트
playerTurtles = []          # 그리기 작업할 거북이들 100마리
swidth, sheight = 500, 500  # 윈도우 크기

turtle.title("거북이 리스트")
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)

# 난수를 통해서 거북이들의 값을 구하기
shapeList = turtle.getshapes()      # 거북이의 도형등을 읽어와 저장

for i in range(0, 100):
    random.shuffle(shapeList)                               # 거북이의 도형 순서를 섞는다.(셔플)
    myTurtle = turtle.Turtle(shapeList[0])                  # 첫번째 도형으로 거북이 지정
    tX = random.randrange(int(-swidth/2), int(swidth/2))    # X좌표를 난수로 구하기
    tY = random.randrange(int(-swidth/2), int(swidth/2))    # Y좌표를 난수로 구하기
    r = random.random()                                     # 3원색을 난수로 구하기
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 3)                    # 선 굵기를 난수로 구하기
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])    # 각 거북이 변수에 난수값 추가
print(playerTurtles)

# 거북이들을 이용해서 그리기
# [[1], [2], [3], [4]] ==> [1]
for tList in playerTurtles:     # 2차원 리스트에 저장된 내용을 각 리스트별로 tList에 전달
    myTurtle = tList[0]                             # 도형
    myTurtle.color((tList[4], tList[5], tList[6]))  # 색상
    myTurtle.turtlesize(tList[3])                   # 크기
    myTurtle.goto(tList[1], tList[2])               # 위치

turtle.done()