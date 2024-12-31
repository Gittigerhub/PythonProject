from tkinter import *
win = Tk()

# 이미지 파일을 읽어서 메모리에 저장
photo = PhotoImage(file="GIF/dog.gif")
photo2 = PhotoImage(file="GIF/dog2.gif")
label1 = Label(win, image=photo)
label2 = Label(win, image=photo2)

label1.pack()       # 방향변경 가로 출력 해보기
label2.pack()
win.mainloop()