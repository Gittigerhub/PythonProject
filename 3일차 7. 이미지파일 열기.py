# 파일열기 대화상자를 이용해서 해당 이미지를 읽어서 화면에 출력하는 프로그램

from tkinter import *
from tkinter.filedialog import *

# 파일 열기 함수
def func_open():
    filename = askopenfilename(parent=window, filetypes=(
        ("GIF 파일", "*.gif"),
        ("모든 파일", "*.*")
    ))
    photo = PhotoImage(file=filename)                # 선택한 파일로 이미지 읽기
    label1.configure(image=photo)
    label1.image = photo

# 프로그램 종료 함수
def func_close():
    window.quit()
    window.destroy()

# 프로그램 시작
window = Tk()

# 프로그램 구성
window.geometry("500x500")
window.title("이미지 출력")

photo = PhotoImage()                                 # 빈 이미지 파일 생성
label1 = Label(window, image=photo)                  # 레이블에 이미지 적용
label1.pack(expand=1, anchor=CENTER)                 # 레이블을 가운데 정렬

# 메뉴 구성
mainMenu = Menu(window)
window.config(menu=mainMenu)                         # 메뉴바 구성

fileMenu = Menu(mainMenu)                            # 주메뉴
mainMenu.add_cascade(label="파일", menu=fileMenu)     # 주메뉴 항목과 메뉴 연결

# 부메뉴
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_close)

window.mainloop()