"""
        윈도우
        창으로 구성
        객체(오브젝트)                   : 위젯    ==>     함수와 변수로 구성
        객체 안에 있는 꾸며주는 변수는     : 속성
        스프링부트                       : 오브젝트(화면X) -> 속성 -> Getter, Setter 함수
"""

from tkinter import *                      # 윈도우 라이브러리

win = Tk()                                 # 윈도우 생성
win.geometry("300x300")                    # 윈도우 크기    "가로x세로"
win.title("창의 제목")
win.resizable(width=FALSE, height=TRUE)    # 크기 변경 / true 가능, false 불가능

win.mainloop()                             # 윈도우 창 실행