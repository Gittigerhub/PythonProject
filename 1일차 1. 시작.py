# Python은 파일 만들때 한글 띄어쓰기 아무상관이 없다.

# 주석 처리

"""
다중 주석
주석, 문자열 값 = 두 가지가 됨
문자열 값으로는 앞에 변수가 있으면 됨
"""

"""
콘솔 프로그램은 표준 입출력 명령
입력 : input(), scanner(java), scanf(c++)
출력 : print(), print(java), printf(c++)
"""

# 변수는 데이터형이 존재하지 않는다.  javascript처럼 들어오는 값이 데이터형을 결정
# 변수명, let 변수명(javascript), Integer 변수명(java), int 변수명(c++)

# 문법 규칙 : 블럭지정이 없다. 블럭은 들여쓰기로 구분한다. tab으로 들여쓰기 사용
a = input() # 키보드로 입력받은 값을 a에 저장, 모든 입력은 문자로 처리
b = input()

result = a + b # 연산

print(result) # 콘솔로 출력
# input을 변수에 담았기 때문에 실행 시, 값을 입력해줘야 한다.