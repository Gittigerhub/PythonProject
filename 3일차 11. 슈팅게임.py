"""
        상단의 괴물을 우주선의 미사일로 격추하는 게임
        괴물은 좌에서 우로 임의의 속도로 이동한다.
        괴물이 우측 끝에 도달하면 새로운 괴물이 좌에서 우로 이동한다.
        스페이스바를 통해서 미사일이 발사되고, 미사일이 상단을 벗어나면, 다음 미사일 발사가 가능
        우주선은 상하좌우 이동이 가능합니다.

        1. 화면 구성
        2. 우주선 구현
        3. 괴물 출현 및 동작
        4. 우주선에 미사일 발사
        5. 미사일과 괴물의 충돌체크 -> 점수 증가
"""
from os import write

import pygame       # 게임 라이브러리
import random       # 괴물의 위치 및 속도를 난수로 체크
import sys          # 타이머를 이용해서 다음동작

def paintEntity(entity, x, y):                   # 해당위치에 객체를 출력하는 함수
    monitor.blit(entity, (int(x), int(y)))  # 윈도우 창에 지정된 위치에 객체를 출력 / 나중에 오류가 안 뜨려면 정수로 받아야 함

def playGame():     # 게임 구현부
    global monitor, ship, monster, fireCount

    # 난수로 색상 선택
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    # 우주선의 초기 위치
    shipX = swidth/2        # 가로는 중앙에
    shipY = sheight*0.8     # 하단 부분에
    dx, dy = 0, 0           # 이동 값(좌우상하 키를 눌렀을 때 이동할 거리 값)

    # 몬스터 작업
    monster = pygame.image.load(random.choice(monsterImage))    # 난수로 몬스터를 선택
    monstersize = monster.get_rect().size
    monsterX = 0
    monsterY = random.randrange(0, int(swidth*0.3))        # 높이는 폭에 30% 내외
    monsterSpeed = random.randrange(1, 5)             # 이동속도

    # 미사일 작업(미사일 발사 준비 상태)
    missileX, missileY = None, None

    # 우주선, 미사일, 괴물 이동 및 동작
    while True:
        (pygame.time.Clock()).tick(50)  # 지연 시간  /  1000이 1초
        monitor.fill((r, g, b))         # 배경색 지정

        for e in pygame.event.get():    # 이벤트 값을 읽어온다. (동시 키인식)
            if e.type in [pygame.QUIT]: # 키보드 및 마우스 이벤트 시, 종료
                pygame.quit()
                sys.exit()

            # 우주선 키조작 이벤트
            if e.type in [pygame.KEYDOWN]:      # 키보드를 눌렀을 때
                if e.key == pygame.K_LEFT:      # 왼쪽 키를 눌렀을 때
                    dx = -5
                if e.key == pygame.K_RIGHT:     # 오른쪽 키를 눌렀을 때
                    dx = 5
                if e.key == pygame.K_UP:        # 위쪽 키를 눌렀을 때
                    dy = -5
                if e.key == pygame.K_DOWN:      # 아래쪽 키를 눌렀을 때
                    dy = 5
                if e.key == pygame.K_SPACE:     # 스페이스바 키를 눌렀을 때
                    # 미사일이 나가는 위치 (우주선 상단에 가운데 위치)
                    if missileX == None:        # 미사일이 발사되지 않았으면
                        missileX = shipX + shipsize[0]/2
                        missileY = shipY
            if e.type in [pygame.KEYUP]:        # 키보드를 떼었을 때
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or\
                        e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    dy = dx = 0                 # 방향 키를 떼었을 때 이동값은 0으로

        # 유효성 검사(우주선이 이동할 수 있는 범위)
        if (0<shipX+dx and shipX+dx <= swidth - shipsize[0]) \
                and (sheight / 2 < shipY+dy and shipY+dy <= sheight - shipsize[1]):
                                                    # 이동시 좌우 범위 안에 들어가면
            shipX += dx                             # 우주선 이동
            shipY += dy

        paintEntity(ship, shipX, shipY)         # 우주선을 화면에 출력

        # 몬스터 작업
        monsterX += monsterSpeed

        # 유효성 검사(몬스터가 오른쪽 끝까지 갔을 때)
        if monsterX > swidth:
            monsterX = 0                                                 # 넘어갈 때 다시 원점으로 이동
            monsterY = random.randrange(0, int(swidth*0.3))         # 세로 위치 랜덤 변경
            monster = pygame.image.load(random.choice(monsterImage))     # 원점으로 이동 될 때 이미지 바뀜
            monstersize = monster.get_rect().size                        # 원점으로 이동 될 때 사이즈 바뀜
            monsterSpeed = random.randrange(1, 5)              # 원점으로 이동 될 때 속도 바뀜

        paintEntity(monster, monsterX, monsterY)

        # 미사일 이동
        if missileX != None:                    # 미사일이 발사 되었으면
            missileY -= 10                      # 위로 10만큼 이동
            # 유효성 검사
            if missileY < 0:                    # 미사일이 화면에서 벗어나면
                missileX, missileY = None, None
            else:                               # 미사일의 값이 지워지면 아래 코드가 성립할 수 없기 때문에 오류가 나서 else 처리
                paintEntity(missile, missileX, missileY)

        # 미사일과 몬스터의 충돌 체크
        if missileX != None:            # 미사일이 발사중이면
            # 몬스터 폭안에 미사일이 들어가 있고, 몬스터 높이 안에 포함이 되면 충돌
            if (monsterX < missileX and missileX < monsterX + monstersize[0]) \
                    and (monsterY<missileY and missileY < monsterY + monstersize[1]):
                fireCount += 1          # 점수 증가

                # 몬스터 제거 -> 재등장
                monster = pygame.image.load(random.choice(monsterImage))
                monstersize = monster.get_rect().size
                monsterX = 0
                monsterY = random.randrange(0, int(swidth*0.3))
                monsterSpeed = random.randrange(1, 5)

                # 미사일 제거
                missileX, missileY = None, None

        # 점수판에 점수 출력
        writeScore(fireCount)

        pygame.display.update()                 # 화면을 갱신 (적 이동, 미사일 이동, 우주선 이동)

def writeScore(count):
    myfont = pygame.font.Font("NanumGothic.ttf", 20)    # 사용할 글꼴
    txt = myfont.render("Score: " + str(count), True, (255-r, 255-g, 255-b))
    monitor.blit(txt, (10, sheight-40))

# 전역 변수
r, g, b = 0, 0, 0           # 배경 색상을 위한 색
swidth, sheight = 500, 700  # 윈도우 크기
monitor = None              # 게임 화면
ship, shipsize = None, 0    # 우주선과 크기를 저장할 변수

# 몬스터
monsterImage = ['monster01.png', 'monster02.png', 'monster03.png', 'monster04.png', 'monster05.png',
                'monster06.png', 'monster07.png', 'monster08.png', 'monster09.png', 'monster10.png']
monster = None      # 적용할 몬스터 이미지

# 미사일
missile = None

# 점수판
fireCount = 0

# 메인
pygame.init()                                           # 게임 초기화
monitor = pygame.display.set_mode((swidth, sheight))    # 게임 화면
pygame.display.set_caption("슈팅 게임")

# 우주선 불러오기
ship = pygame.image.load("ship01.png")      # 그림 파일 읽기
shipsize = ship.get_rect().size             # 우주선의 크기를 저장

# 미사일 이미지
missile = pygame.image.load('missile.png')

playGame()                                              # 게임을 구동