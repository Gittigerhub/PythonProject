import operator # 모듈은 파이썬에서 수행 가능한 연산을 효율적으로 처리할 수 있는 함수를 모아놓은 것

singer = {}     # 딕셔너리를 생성

singer['이름'] = '트와이스'       # 딕셔너리에 키와 값을 추가
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

print(singer.keys())
for k in singer.keys():                 # 키를 하나씩 읽어서 반복
    print("%s ==> %s" %(k, singer[k]))  # 해당키와 값을 출력

# 딕셔너리 정렬
trainDict, trainList = {}, []           #  딕셔너리와 리스트를 생성

trainDict = {'Thomas':'토마스', 'Edward':'에드워드',\
             'Henry':'헨리', 'Gothen':'고든', 'James':'제임스'}

# 키를 기준으로 정렬해서 결과를 리스트에 저장
trainList = sorted(trainDict.items(),key=operator.itemgetter(0))
print(trainDict)
print(trainList)