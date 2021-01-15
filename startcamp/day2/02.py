# Dictionery (딕셔너리) - 궁극의 자료형, 각각의 인덱스 존재하지 않고 key로 접근, 순서없음

my_home = {
    'location' : 'seoul',
    'area-code' : '02'
}

# 딕셔너리 원소 접근
# 1
print(my_home['location'])
# print(my_home['name'])
# 2 
print(my_home.get('location'))
print(my_home.get('name'))  # None 자료가 없다는 것을 표현해주는 자료형

