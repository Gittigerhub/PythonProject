# 체크상자 : 하나의 항목의 상태를 저장할 때 0-(해제, 1-체크)
## 라이브러리
from tkinter import *
from tkinter import messagebox

# 함수부
def myFunc():
    # variable에 선언된 변수가 함수에 자동 전달
    if chk.get() == 0:
        messagebox.showinfo("메세지", "체크가 해제되었습니다.")
    else:
        messagebox.showinfo("메세지", "체크가 설정되었습니다.")

def myFunc2():
    if opt.get() == 1:
        # Pack()으로 화면에 출력된 경우 일반 작업으로 화면 갱신이 안된다.
        # 이미 화면에 뜬 객체를 수정할 때는 configure(변경할 속성명="변경값", ...)으로 수정
        label1.configure(text="파이썬")
    elif opt == 2:
        label1.configure(text="C++")
    else:
        label1.configure(text="JAVA")


## 메인
window = Tk()       # 생성
chk = IntVar()      # 정수형 변수로 선언(체크박스용)
opt = IntVar()      # 정수형 변수로 선언(라디오 단추용)

# 체크박스별 변수명을 다르게 사용
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)   # 체크상태를 저장할 변수지정 필수
cb1.pack()

# 라디오 단추는 변수명은 동일하게, 값은 다르게 성정해서 사용
rb1 = Radiobutton(window, text="파이썬", variable=opt, value=1, command=myFunc2)
rb2 = Radiobutton(window, text="C++", variable=opt, value=2, command=myFunc2)
rb3 = Radiobutton(window, text="JAVA", variable=opt, value=3, command=myFunc2)

label1 = Label(window, text="선택한 언어")
btn1 = Button(window, text="버튼")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()
btn1.pack(side=TOP, fill=X, padx=5, pady=5)

window.mainloop()