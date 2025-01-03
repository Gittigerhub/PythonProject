"""
        왼쪽여백 스페이스바 이동, 오른쪽은 내용이 없으면 빈공백
        행은 9행, 별 1, 3, 5, 7, 9, 7, 5, 3, 1 / 여백 4, 3, 2, 1, 0, 1, 2, 3, 4

        0행            *
        1행           ***
        2행          *****
        3행         *******
        4행        *********
        5행         *******
        6행          *****
        7행           ***
        8행            *

        변수하는 값을 가지고 규칙(알고리즘)
        행에 대한 while                     0 1 2 3 4 5 6 7 8
        증가와 감소를 처리하는 if 문
                    마름모 아래부분은 5~8에서 4를 빼준다 1 2 3 4
                      최대 개수에서 빼기 4 - 0 1 2 3 4
        빈 공백을 만드는 while               4 3 2 1 0 1 2 3 4
                    마름모 아래부분은 최대수인 8애서 -2 -4 -6 -8
                          늘어나는 개수 2 * 0 2 4 6 8         + 1
        별을 만드는 while                   1 3 5 7 9 7 5 3 1
"""

i, k = 0, 0
while i < 9:                    # 증가되는 모양
    if i < 5:
        # 빈공백
        k = 0
        while k < 4 - i:        # 4, 3, 2, 1, 0
            print(' ', end='')  # print와 print를 연결해서 사용 end
            k += 1
        # 별
        k=0
        while k < 2 * i +1:     # 1, 3, 5, 7, 9
            print('\u2605', end='')
            k += 1

    else:                       # 별이 감소
        k=0
        while k < i - 4:        # 1, 2, 3, 4
            print(' ',end='')
            k+=1

        k=0
        while k < (8-i)*2+1:    # 7, 5, 3, 1
            print('\u2605', end='')
            k += 1

    print()                 # 줄바꿈 처리를 위한 출력문
    i += 1