# 표준 출력장치 print()
print("문자열 출력")
print(123)
print("문자열" + "문자열")
print(123 + 123)
print(str(123) + "문자열") # 파이썬에 +연산자 사용시 좌우 데이터형이 동일 해야만 한다.

# 포멧 형식 %c, %s, %d, %i, %f
# %전체수.소수점자리수 데이터형
# 출력할 데이터형과 위치를 지정하고 값으로 대응
print("%d + %d" %(1220,300))    # 인수 값이 2개이상이면 (변수, 변수, ...) (안에)
print("%d" %123)    # 인수 값이 하나이면 ()생략가능
print(123,23,34)
print(324, "연습", "문자열")
print("01234")
print("%05d" %123)  # 변수 길이 5중에 빈곳은 앞에서 부터 0으로 채운다
print("%5d" %123)   # 변수 길이 5중에 빈곳은 앞에서 부터 빈칸으로 채운다
print("%-5d" %123)  # 변수 길이 5중에 빈곳은 뒤에서 부터 빈칸으로 채운다