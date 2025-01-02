"""
        키보드 이벤트
        <Key>                                                       : 모든키

        <Return>, <BackSpace>, <Tab>, <Shift_L>, <Shift_R>, ...     : 특수키

        <Up>, <Down>, <Left>, <Right>, <F1>~<F12>
        a~z, A~Z, <space>, <less>                                   : 일반키

        <Shift-Up>, <Shift-Down>, ...                               : 조합키
"""

from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    # keycode는 ASCII코드 값으로 뱉어냄  A => 65 ===> chr() : ASCII코드를 문자로 변환
    messagebox.showinfo("키보드 이벤트", "눌린키:" + chr(event.keycode) + "," + str(event.keycode))

window = Tk()

# 이벤트
window.bind("<Key>", keyEvent)      # 키보드 이벤트

window.mainloop()