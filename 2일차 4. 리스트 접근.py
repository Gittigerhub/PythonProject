"""
        슬라이딩
        [시작:끝]          : 지정된 위치에서 끝 전까지 읽어온다.
        [시작:]           : 지정된 위치에서 마지막까지 읽어온다.
        [:끝]             : 처음부터 끝 전까지 읽어온다.
        [:]               : 모든 값을 읽어온다.
        [시작:끝:증가값]    : 시작 값으로 부터 증가 값만큼 이동하면서 끝 전까지 읽어온다. (for문이랑 비슷하다.)
        [::2]             : 시작에서 2칸씩 이동하면서 값을 읽어온다.
        [-:]              : 음수를 표시하면 뒤에서 부터 읽어온다.

        -5 -4 -3 -2 -1 -0 0 1 2 3 4 5 -0이 있을수가 없으니 ==> -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 0이 양수에 포함되어 음수가 1 더 크다.

        0   1   2   3   4   5       => 리스트 양수 위치
        [12, 12, 45, 87, 65, 45]    => 리스트
        -6  -5  -4  -3  -2  -1      => 리스트 음수 위치
"""
aa = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("리스트 전체 값 출력 : ", aa)
print("aa[1:4] = ", aa[1:4])
print("aa[:4] = ", aa[:4])
print("aa[1:] = ", aa[1:])
print("aa[:] = ", aa[:])
print("aa[0:7:2] = ", aa[0:7:2])
print("aa[-3:] = ", aa[-3:])
print("aa[2] = ", aa[2])
print("aa[-2] = ", aa[-2])

aa[0] = 100
print("aa=", aa)
aa[1:2] = [200, 300]
print("aa=", aa)