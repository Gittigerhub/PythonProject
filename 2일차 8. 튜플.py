"""
        튜플은 읽기만 가능!
        1차원, 2차원, 다차원 튜플도 가능
        슬라이딩 사용도 가능 -> 읽기 기능은 리스트와 동일
"""

tt1 = (10, 20, 30)          # 튜플로 10, 20, 30을 저장
tt2 = 10, 20, 30
print(tt1)
print(tt2)

"""
        튜플은 내용 변경 작업 불가능 -> 코드 에러 뜸
        tt1.remove(10)
        tt1[0] = 40

        그럼 튜플은 언제 써야 하나??
        튜플은 프로그램 구현 시, 고정 값을 지정할 때 사용
        예)  게임 에너지(100), 케릭터(2)        
"""

print(tt1[:])
print(tt1[1:])
print(tt1[:2])