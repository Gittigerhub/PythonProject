# 윈도우에서 마우스 버튼을 클릭했을 때 마우스 커서의 좌표를 출력하는 프로그램
from tkinter import *

def mouseClick(event):          # 마우스를 클릭했을 때의 이벤트 처리 메소드
    txt=""                      # 좌표를 출력하기 위한 변수
    if event.num == 1:          # 왼쪽 버튼을 클릭했을 때
        txt = "마우스 왼족 버튼이 ("
    elif event.num == 3:        # 오른쪽 버튼을 클릭했을 때
        txt = "마우스 오른쪽 버튼이 ("

    # txt 내용에 새로운 문자열 추가 (+=)
    txt += str(event.x) + ", " + str(event.y) + ") 에서 클릭되었습니다."
    label1.configure(text=txt)

window = Tk()
window.geometry("400x400")      # x는 영문자 소문자로 x
label1 = Label(window, text="좌표가 출력될 부분")
label1.pack(expand=1, anchor=CENTER)

# 이벤트
window.bind("<Button>", mouseClick)

window.mainloop()