# 문자열을 입력 받아서 역으로 출력하는 프로그램
inStr, outStr = '', ''      # inStr -> 입력받은 문자열을 저장할 변수
                            # outStr -> 거꾸로 문자열을 조립해서 지정할 변수
count = 0                   # 전체 문자열의 길이를 저장할 변수

inStr = input("문자열을 입력하세요?")
count = len(inStr)          # 입력받은 문자열의 길이를 저장

# 연습프로그램 => '램', '그', '로', '프', '습', '연' => 램그로프습연
# 0 1 2 3 4 5 => i
# 최대값-위치 => 역순
#              램 그 로 프 습 연
# 6 - i - 1 => 5, 4, 3, 2, 1, 0
for i in range(0, count):               # 문자열의 길이만큼 반복
    outStr += inStr[count - i - 1]      # 연습프로그램
print(outStr)

"""
        주요 함수
        upper()                             : 소문자를 대문자러 변환
        lower()                             : 대문자를 소문자로 변환
        Title()                             : 각 단어의 첫글자를 대문자로 변환
        swapcase()                          : 대문자는 소문자로 소문자는 대문자로 상호 변환
        capitalize()                        : 첫글자만 대문자로 변환
        casefold()                          : 모두 소문자로 변환
        center(전체길이, fillchar='채울문자')  : 기존 문자열을 가운데 배치하고, 나머지 공백에 지정문자로 채운다.
                                                예)  s = "연습"
                                                     s.center(10, fillchar='*') => "****연습****"
        count("문자열")                      : 해당 문자열의 갯수
                                                예)  s = "이 연습 프로그램은 연습을 위한 프로그램입니다."
                                                     s.count("연습") ==> 2
        encode(encoding='문자셋')            : 문자열을 해당 문자셋으로 변환
                                                예)  s = "연습"
                                                     s.encode(encoding='UTF-8')
        endswith("끝문자열")                 : 해당 문자열이 끝에 존재하면 true, 아니면 false
                                                예)  s = "연습용 프로그램 입니다"
                                                     s.endswith("입니다") ==> true
        expandtabs(탭크기)                   : 문자열에 존재하는 tab키를 빈 공백으로 대체
                                                예)  s = "연습용\t프로그램\t입니다."
                                                     s.expandtabs(2) ==>" 연습용  프로그램  입니다."
        find("찾을 문자열")                   : 해당 문자열이 존재하는 위치값을 반환
                                                예)  s = "연습용 프로그램"
                                                     s.find("프로그램") ==> 4
        format("문자열")                     : {}에 문자열로 대체한다.
                                                예)  s = "연습용 {}"
                                                     s.format("프로그램") => "연습용 프로그램"
        index("문자열")                      : 해당 문자열이 존재하는 첫번째 위치를 반환
                                                예) s = "연습을 위한 연습용 프로그램"
                                                     s.index("연습") => 0
                                                     
        isalnum()                           : 문자열이 알파벳과 숫자로 이루어졌으면 true, 아니면 false
        isalpha()                           : 문자열이 알파벳으로 이루어졌으면 true, 아니면 false
        isdigit()                           : 문자열이 숫자로 이루어졌으면 true, 아니면 false
        isspace()                           : 문자열이 빈공백으로 이루어졌으면 true, 아니면 false
        
        lstrip()                            : 왼쪽 여백 제거 / JAVA trim 이랑 비슷 / "    연습" => "연습"
        rstrip()                            : 오른쪽 여백 제거
        strip()                             : 양쪽 여백 제거
        
        replace(기존문자열, 새로운문자열)       : 기존문자열을 찾아 새로운 문자열로 대체
                                                예)  s = "안녕 하세요"
                                                     s.replace("안녕", "환영") => 환영 하세요
"""