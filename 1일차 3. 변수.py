# 변수는 데이터형이 존재하지 않는다.
bVar = True                 # 논리형 변수(True, False)
intVar = 123                # 정수형 변수
floatVar = 3.14             # 실수형 변수
strVar = "hello world"      # 문자열 변수

# 각 순서대로 변수에 값을 적용
bVar, intVar, floatVar, strVar = True, 123, 3.14, "hello world"

print(bVar, intVar, floatVar, strVar)

intVar = intVar2 = intVar3 = 100        # 100을 intVar3에 intVar2에 intVar1에
intVar4, intVar5, intVar6 = [100]*3     # 100을 3번 반복해서 적용

print(intVar, intVar2, intVar3)
print(intVar4, intVar5, intVar6)