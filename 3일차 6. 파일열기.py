from tkinter import *
from tkinter.filedialog import *    # 파일과 관련된 거 작업

window = Tk()
window.geometry("400x400")
label1 = Label(window, text="선택한 파일명")
label1.pack()

# parent=부모창, filetypes=파일유형 => (메세지, 확장자)
# 와일드카드(문자를 대체) : *(모든문자 대체), ?(한문자 대체)
fileName = askopenfilename(parent=window,
                           filetypes=(
                               ("GID파일", "*.gif"),
                               ("JPG파일", "*.jpg"),
                               ("모든 파일", "*.*"),
                           )
)

# pack() 이후에 변경은 configure()
label1.configure(text=str(fileName))

window.mainloop()