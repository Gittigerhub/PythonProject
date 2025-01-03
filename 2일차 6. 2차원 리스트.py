"""
        배열, 리스트는 다차원으로 구성 가능
        업무용 프로그램 3차원(학년, 반, 번호)
        게임 프로그램 2차원

        3차원 리스트 = [[[], [], []], [[], [], []], [[], [], []]]
        2차원 리스트 = [[], [], []]  ==> 행렬 ==> 리스트에 리스트를 추가

        2차원 리스트 인수 [행][열]
        [   열  0  1  2
        0행    [1, 2, 3],
        1행    [4, 5, 6],
        2행    [7, 8, 9]
        ]
"""
list1 = []      # 작업할 리스트
list2 = []      # 2차원으로 저장할 리스트   /   JAVA -> list2[][] = new list2[][]
value = 1       # 저장할 시작 값

for i in range(0, 3):           # 행
    for j in range(0, 3):       # 열
        list1.append(value)     # [1, 2, 3], [4, 5, 6], [7, 8, 9]
        value += 1
    list2.append(list1)         # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list1 = []                  # 작업 리스트를 초기화

print(list2)
print(list2[0][1])              # 사용할 때는 반드시 2차원 첨자로 사용해야한다.
# print(list2[5]) => 이렇게 하면 오류 뜸

for i in range(0, 3):           # 행
    for j in range(0, 3):       # 열
        print("%3d" %list2[i][j], end=" ") # 각 행의 열을 옆으로 출력
    print("")   # 행의 열작업 후 다음줄로 이동