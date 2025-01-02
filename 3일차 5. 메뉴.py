"""
        윈도우 창에
        메뉴바 구성
        메인메뉴
        서브메뉴

        메뉴바 = Menu(윈도우창) - 메뉴바를 위도우창 에 적용
        윈도우창.config(menu=메뉴바)
        메인메뉴 = Menu(메뉴바) - 메인메뉴를 메뉴바에 적용
        메뉴바.add_cascade(label="메뉴명", menu=메인메뉴) - 메인메뉴에 항목 추가
        메인메뉴.add_command(label="서버메뉴명", command=함수)
"""

from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *  # 대화상자

def func_open():
    value = askinteger("수를 입력", "수를 입력하세요", minvalue=0, maxvalue=100)   # 정수 입력받음

def func_exit():
    window.quit()           # 현재 윈도우 창을 닫기
    window.destroy()        # 메모리상에 윈도우 창을 제거

window = Tk()

mainMenu = Menu(window)     # 윈도우에 메뉴바
window.config(menu=mainMenu)

# 메인메뉴
fileMenu = Menu(mainMenu)   # 메뉴바에 추가
mainMenu.add_cascade(label="파일", menu=fileMenu) # 파일은 fileMenu연결해서 메뉴바에 출력

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="편집", menu=editMenu)

# 서브메뉴 추가
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()                         # 구분선
fileMenu.add_command(label="종료", command=func_exit)

window.mainloop()