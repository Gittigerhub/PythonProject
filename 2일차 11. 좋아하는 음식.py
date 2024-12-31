foods = {
    '떡볶이':'오뎅', '짜장면':'단무지', '라면':'김치', '피자':'피클',
    '맥주':'땅콩', '치킨':'치킨무', '삼겹살':'상추'
}

while(True):        # 무한반복
    myFoot = input(str(list(foods.keys())) + "중 좋아하는 음식은?")

    # 종료 판단(유효성 검사)
    if myFoot == '끝':
        break

    if myFoot in foods:     # 입력한 내용이 딕셔너리에 존재하면
        print("<%s> 궁합 음식은 <%s>입니다." %(myFoot, foods[myFoot]))
    else:
        print("해당하는 음식이 없습니다.")