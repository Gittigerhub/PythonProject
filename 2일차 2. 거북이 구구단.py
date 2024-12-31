"""
        2단부터 9단까지 가로형으로 출력하는 구구단
        거북이에 문자출력 명령을 이용해서 작성
        2단 1~9, 3단 1~9, 4단 1~9, 5단 1~9, ...
        단수는 2~9 반복, 차수는 단수마다 1~9 반복
"""

import turtle

tX, tY = [0] * 2                                    # tX, tY에 0을 저장, 거북이의 좌표를 기억할 변수
switdh, sheight = 800, 450                          # 윈도우의 크기

turtle.title("거북이 구구단")
turtle.shape("turtle")
turtle.setup(width=switdh+50, height=sheight+50)    # 윈도우 크기
turtle.screensize(switdh, sheight)                  # 작업영역(캔버스)
tX = -500                                           # 왼쪽 끝
tY = 250                                            # 상단
turtle.penup()
turtle.goto(tX, tY)                                 # 이동

# 구구단 작업
for i in range(1, 10):                              # 차수(행)
    for j in range(2, 10):                          # 단수(열)
        gugudan = str(j)+" X "+str(i)+" = "+str(i*j)
        turtle.goto(tX+80*j, tY-40*i)
        turtle.write(gugudan, font=("Arial", 12, "bold"))

turtle.done()