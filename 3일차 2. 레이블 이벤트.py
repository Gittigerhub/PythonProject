from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "토끼 레이블에서 마우스를 클릭했습니다.")

win = Tk()

# 이미지 일기
photo = PhotoImage(file="GIF/rabbit2.gif")
label1 = Label(win, image=photo)
label1.pack()                           # 배치

# 이벤트
label1.bind("<Button>", clickImage)     # 레이블에 이벤트를 적용

win.mainloop()