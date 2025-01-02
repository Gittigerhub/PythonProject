"""
        pillow 라이브러리를 이용해서 pillow에 제공하는 기능으로 간단한
        이미지 편집 프로그램

        메뉴 구성
        -------
        파일 - 파일 열기, 파일 저장, 프로그램 종료
        이미지처리(1) - 확대(축소), 상하반전(좌우반전), 회전
        이미지처리(2) - 밝게(어둡게), 블러링, 엠보싱, 흑백이미지
"""

from tkinter import *
from tkinter.filedialog import *                                # 파일 열기/저장
from tkinter.simpledialog import *                              # 밝게/어둡게, 회전 각도
from PIL import Image, ImageFilter, ImageEnhance, ImageOps      # 이미지 효과
from PIL.ImageOps import expand


# 함수
def func_open():                        # 파일 열기
    global window, canvas, paper, photo1, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(
        ("모든 그림 파일", "*.jpg;*.gif;*.bmp;*.png;*.tif;"),
        ("모든 파일", "*.*")
    ))
    # 원본 이미지
    photo1 = Image.open(readFp).convert("RGB")          # 픽셀 단위로 이미지를 변환
    oriX = photo1.width                                 # 그림의 크기를 저장
    oriY = photo1.height

    # 작업을 위한 복사본
    photo2 = photo1.copy()                              # 이미지 복사
    newX = photo2.width                                 # 작업 이미지 크기
    newY = photo2.height

    displayImage(photo2, newX, newY)                    # 작업 이미지를 화면에 출력

def func_save():                        # 파일 저장
    global window, canvas, paper, photo1, photo2, oriX, oriY
    if photo2 == None:      # 작업한 이미지 또는 불러온 이미지가 없으면
        return              # 종료
    # R -읽기, W -쓰기, W+ -추가
    # defaultextension (확장자 생략 시, 기본 적용 확장자)
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(
        ("JPG 파일", "*.jpg;*.jpeg"),
        ("모든 파일", "*.*")
    ))
    photo2.save(saveFp.name)

def func_close():                       # 윈도우 종료
    window.quit()
    window.destroy()

def displayImage(img, width, height):   # 윈도우 창에 이미지 출력
    global window, canvas, paper, photo1, photo2, oriX, oriY
    # 이미지 크기에 맞게 윈도우 창 크기를 변경
    window.geometry(str(width) + "x" + str(height))
    if canvas != None:      # 유효성 검사(기존에 작업한 내용이 있으면 초기화)
        canvas.destroy()    # 작업지 삭제

    canvas = Canvas(window, width=width, height=height)    # 작업지를 윈도우에 적용

    # 캔버스에 출력할 이미지 작업
    paper = PhotoImage(width=width, height=height)  # 이미지 저장을 위한 초기화
    canvas.create_image((width/2, height/2), image=paper, state="normal")

    rgbString = ""  # 이미지 데이터 변수(행/열)
    rgbImage = img.convert("RGB")   # 전달 받은 이미지를 RGB 형식으로 변환
    for i in range(0, height):      # 행
        tmpString = ""  # 한 행의 픽셀들을 저장할 변수

        for j in range(0, width):   # 열
            r, g, b = rgbImage.getpixel((j, i))          # 한점(픽셀)의 색상을 읽어와서 저장
            tmpString += "#%02x%02x%02x " %(r, g, b)     # 옆으로 나열되는 애들은 꼭 띄어쓰기 추가해줘야 구분됨

        rgbString += "{" + tmpString + "} "  # 행들을 결합 # 옆으로 나열되는 애들은 꼭 띄어쓰기 추가해줘야 구분됨
    paper.put(rgbString)    # 작업지에 이미지를 출력
    canvas.pack()

def func_zoomin():                      # 확대/축소
    global window, canvas, paper, photo1, photo2, oriX, oriY
    # 확대 값을 대화상자로 입력
    scale = askinteger("확대", "확대할 배율(2~4)을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo1.copy()  # 원본을 복사
    photo2 = photo2.resize((int(oriX*scale), int(oriY*scale)))
    newX = photo2.width     # 새로 변경된 크기의 이미지 사이즈 저장
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_zoomout():                     # 확대/축소
    global window, canvas, paper, photo1, photo2, oriX, oriY
    # 축소 값을 대화상자로 입력
    scale = askinteger("축소", "축소할 배율(2~4)을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo1.copy()  # 원본을 복사
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))
    newX = photo2.width  # 새로 변경된 크기의 이미지 사이즈 저장
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror1():                     # 좌우/상하 뒤집기
    global window, canvas, paper, photo1, photo2, oriX, oriY
    photo2 = photo1.copy()  # 원본 복사
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror2():                     # 좌우/상하 뒤집기
    global window, canvas, paper, photo1, photo2, oriX, oriY
    photo2 = photo1.copy()  # 원본 복사 # photo2 = photo2.copy() 이렇게 코드를 작성하면 그상태의 반전을 계속 적용할 수 있음
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rotate():                      # 회전
    global window, canvas, paper, photo1, photo2, oriX, oriY
    # 회전할 각도를 입력 대화상자
    degree = askinteger("회전", "회전할 각도(0~306)를 입력하세요?", minvalue=0, maxvalue=360)
    photo2 = photo1.copy()  # 원본 복사
    photo2 = photo2.rotate(degree, expand=True)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bright():                      # 밝게
    global window, canvas, paper, photo1, photo2, oriX, oriY
    # 밝기를 입력할 대화상자
    value = askinteger("밝게", "값(1~10)을 입력하세요?", minvalue=1, maxvalue=10)    # 1은 기본 밝기
    photo2 = photo1.copy()  # 원본 복사
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_dark():                        # 어둡게
    global window, canvas, paper, photo1, photo2, oriX, oriY
    # 어둡기를 입력할 대화상자
    value = askfloat("어둡게", "값(0.0~1.0)을 입력하세요?", minvalue=0.0, maxvalue=1.0)  # 1은 기본 밝기
    photo2 = photo1.copy()  # 원본 복사
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_blur():                        # 블러
    global window, canvas, paper, photo1, photo2, oriX, oriY
    photo2 = photo1.copy()  # 원본 복사
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_embo():                        # 엠보싱
    global window, canvas, paper, photo1, photo2, oriX, oriY
    photo2 = photo1.copy()  # 원본 복사
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bw():                          # 흑백 이미지
    global window, canvas, paper, photo1, photo2, oriX, oriY
    photo2 = photo1.copy()  # 원본 복사
    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

# 이미지 읽기 -> 픽셀단위로 저장(paper) -> 효과적용(canvas) 출력
# 모든 효과는 원본(paper)로 작업 진행

# 전역 변수
window, canvas, paper = None, None, None    # 윈도우, 출력용 작업지, 작업용
photo1, photo2 = None, None                 # 원본 이미지, 결과 이미지
oriX, oriY = 0, 0                           # 원본 이미지의 크기

## 메인 프로그램(윈도우, 오브젝트 배치, 메뉴 구성)
window = Tk()
window.title("미니 포토샾")
window.geometry("250x250")

# 구성 요소
# 메뉴
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_close)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=imageMenu)
imageMenu.add_command(label="확대", command=func_zoomin)
imageMenu.add_command(label="축소", command=func_zoomout)
imageMenu.add_separator()
imageMenu.add_command(label="상하 반전", command=func_mirror1)
imageMenu.add_command(label="좌우 반전", command=func_mirror2)
imageMenu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="블러링", command=func_blur)
image2Menu.add_command(label="엠보싱", command=func_embo)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)

window.mainloop()