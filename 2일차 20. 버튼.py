"""
        버튼은 윈도우창에 동작을 지시할 때
        Label로 속성과 동일하게 속성을 적용가능
        추가된 부분은 command=작업지정(사용자가 만든 함수, 예약어를 통해서도 작업 가능)
"""

from tkinter import *
from tkinter import messagebox      # 메세지창, Javascript alert랑 비슷

def myFunc():
    # 알림창("제목", "문자열")
    messagebox.showinfo("고양이 버튼", "강아지 버튼을 눌렀습니다.")

# ======================================================================================

win = Tk()
photo = PhotoImage(file="GIF/cat2.gif")     # 이미지를 읽기
button = Button(win, image=photo, command=myFunc)   # 함수명()으로 기입하면 바로 실행되고, 함수명만 기입할 경우 대기상태로 창이 뜬다.

button.pack()
win.mainloop()