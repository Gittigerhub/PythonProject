import turtle
import random
from tkinter.simpledialog import *      # 윈도우 라이브러리 (대화상자 일부분) / 특정한 패키지 안에 내용을 가져올때 from

# set~      : 받은 인수 값을 저장하는 목적
# get~      : return으로 결과 값을 전달
# is        : 함수내에 if문으로 true, false의 비교 결과값 전달
# 일반적인 동작함수는 명사로 구성
def getAskStr():
    # 문자열을 변수에 저장 후 변경없이 결과처리할 때는 변수가 불필요
    return askstring("문자열 입력", "문자열을 입력하세요.")

def getColor():
    # 한행에 여러 문장을 표현할 때 ;을 사용한다.
    r = random.random(); g = random.random(); b = random.random()
    return (r, g, b)

def getXYS(swidth, sheight):
    tX = random.randrange(int(-swidth / 2), int(swidth / 2))
    tY = random.randrange(int(-sheight / 2), int(sheight / 2))
    txtSize = random.randrange(10, 50)
    return (tX, tY, txtSize)

inStr = ""                                              # 입력받은 문자열을 저장할 변수
swidth, sheight = 300, 300                              #  윈도우 크기

tX, tY, txtSize = [0] * 3                               # 난수로 생성할 위치, 글자 크기를 저장할 변수

turtle.title("거북이 문자열 출력")
turtle.shape("turtle")
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()                                          # 선그리기 해제

# askstring("창제목", "문자열") => 문자열 입력 대화상자
inStr = getAskStr()

for ch in inStr:                                        # 문자열을 한글자씩 분리해서 반복
    # 작업에 필요한 값들을 난수로 완성
    tX, tY, txtSize = getXYS(swidth, sheight)
    r, g, b = getColor()

    turtle.goto(tX, tY)                                 # 출력할 위치로 거북이를 이동
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=("Arial", txtSize, 'bold'))   # 해당 문자를 출력

turtle.done()