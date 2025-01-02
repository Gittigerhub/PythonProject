"""
        강아지, 고양이, 토끼를 옵션 단추로 구성해서 원하는 동물을 선택해서
        사진보기 버튼을 클릭하면 해당이미지를 출력하는 프로그램
"""

from tkinter import *

# 사진보기 버튼시 처리할 함수
def imageClick():
    if var.get() == 1:                  # 해당 옵션단추를 파악해서 이미지를 레이블에 출력
        labelImage.configure(image=photo1)
    elif var.get() == 2:
        labelImage.configure(image=photo2)
    else:                               # 1, 2가 아닌 모든 경우
        labelImage.configure(image=photo3)

var, labelImage = 0, None               # 욥션단추, 이미지
photo1, photo2, photo3 = [None] * 3     # 강아지, 고양이, 토끼 이미지 저장

### 메인
window = Tk()

# 윈도우 명령어기 때문에 window = Tk()를 선언한뒤 작업하지 않으면 오류가 뜬다.
# 작업에 필요한 이미지(시간이 오래걸리는 작업은 초기에 둔다(이유? 창이 다뜬뒤에 시간이 오래걸리는게 후방에 배치되면 화면이 멈춘것으로 착가함))
photo1 = PhotoImage(file="gif/dog10.gif")
photo2 = PhotoImage(file="gif/cat10.gif")
photo3 = PhotoImage(file="gif/rabbit3.gif")

# 화면 구성
window.geometry("400x400")              # 윈도우 크기
window.title("동물 투표")
window.resizable(width=0, height=0)     # 윈도우

labelText = Label(window, text="종아하는 동물 투표", fg="blue", font=("궁서체", 20))
labelText.pack(padx=5, pady=5)          # 여백

var = IntVar()                          # 정수형을 저장할 수 있는 상태로 초기화
rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)

# 버튼
btn = Button(window, text="사진 보기", command=imageClick)
btn.pack(padx=5, pady=5)

# 그림을 출력할 레이블
labelImage = Label(window, image=None, width=200, height=200)
labelImage.pack(padx=5, pady=5)

window.mainloop()