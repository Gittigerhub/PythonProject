"""
        선을 이용해서 그림을 그리는 프로그램
        색상, 선 두께를 지정하여 마우스 눌렀을 때(시작 위치), 마우스 떼었을 때(끝 위치)
        시작과 끝 위치에 선을 그리는 프로그램
        작업지(캔버스) - 그래픽을 작업할 수 있는 작업 영역
"""

from tkinter import *
from tkinter.colorchooser import *      # 색상 대화상자
from tkinter.simpledialog import *      # 입력 대화상자(선 두께 값)

# 선그리기 (x1, y1) - (x2, y2) : 시작과 끝 좌표 사이에 선을 그린다.
### 함수
def mouseClick(event):                  # 마우스를 클릭 시, 시작 좌표 구하기
    global x1, y1
    x1 = event.x                        # 현재 마우스 버튼을 누른 곳의 x 좌표를 저장(시작 좌표)
    y1 = event.y                        # 현재 마우스 버튼을 누른 곳의 y 좌표를 저장(시작 좌표)

def mouseDrop(event):                   # 마우스를 떼었을 때, 끝 좌표 구하고, 선 그리기 작업
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x                        # 현재 마우스 버튼을 누른 곳의 x 좌표를 저장(끝 좌표)
    y2 = event.y                        # 현재 마우스 버튼을 누른 곳의 x 좌표를 저장(끝 좌표)
    # 해당 좌표에 캔버스에 선을 그리는 작업
    canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=penColor)

def getColor():                         # 선택한 색상 값 적용
    # 객체 변수는 자동으로 연결
    # 일반 변수는 수동으로 연결
    global penColor                     # 전역변수를 함수에 호출

    color = askcolor()
    penColor = color[1]                 # 색상 이름을 penColor에 저장

def getWidth():                         # 선 두께 값 지정
    global penWidth

    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue=1, maxvalue=10)

def windowClose():                      # 윈도우 창 종료
    window.quit()
    window.destroy()

# 함수와 메인 프로그램의 변수 전달을 위한 전역 변수
window = None               # 윈도우
canvas = None               # 이미지 작업지
x1, y1, x2, y2 = [None] * 4 # 시작과 끝 좌표
penColor = 'black'          # 선 색
penWidth = 3                # 선 두께

# 메인 프로그램
window = Tk()
window.title("짝퉁 그림판")

## 작업지 구성 및 이벤트
canvas = Canvas(window, height=300, width=300, bg="white")      # 작업지 설정
canvas.pack()                                                   # 윈도우에 작업지 추가

canvas.bind("<Button-1>", mouseClick)                           # 마우스 클릭
canvas.bind("<ButtonRelease-1>", mouseDrop)                     # 마우스 떼었을 때

# 색상과 선 두께 처리를 위한 메뉴
mainMenu = Menu(window)
window.config(menu=mainMenu)
canvasMenu = Menu(mainMenu)                                     # 주메뉴
mainMenu.add_cascade(label="설정", menu=canvasMenu)
canvasMenu.add_command(label="선 색상", command=getColor)
canvasMenu.add_command(label="선 두께", command=getWidth)
canvasMenu.add_separator()
canvasMenu.add_command(label="종료", command=windowClose)

window.mainloop()