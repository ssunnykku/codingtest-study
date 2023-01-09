import operator
#################리스트 만들기#################

# (keys)
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a.keys()
list(a.keys())
# dict_keys(['name', 'phone', 'birth'])
# dict_keys 객체는 리스트를 사용하는 것과 차이가 없지만 리스트 고유의 append, insert, pop, remove, sort함수는 수행할 수 없다.

# (values)

a.values()
# dict_values(['pey', '010-9999-1234', '1118'])

# Key, Value 쌍 얻기(items)

a.items()
# dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
# x튜플로 묶은 리스트를 dict_items 객체로 돌려줌

a.clear()
a
# {}
# 모든 요소 삭제

#################딕셔너리 key 정렬(sorted 이용)##############

# import operator가 필요
test = {"banana": 3, "apple": -3, "carrot": 1}

# 오리지널 딕셔너리
print(f'origin       : {test}\n')

# dictionary.items()
test1 = sorted(test.items())
print(test1)
# [('apple', -3), ('banana', 3), ('carrot', 1)] 오름차순으로 반환해 주지만 이렇게 리스트를 반환한다.
print(f'sorted(test.item())       : {test1}')
# 다시 딕셔너리로
print(f'dict(sorted(test.item())       : {dict(test1)}')

# 키 값만을 빼서 정렬하기
test2 = sorted(test)
print(f'sorted(test)       : {test2}')

# 내림차순 정렬
test3 = sorted(test.items(), reverse=True)
print(test3)

#################딕셔너리 value 정렬##############
# 방법1: operator.itemgetter
# 방법2: lambda(최신)

# 딕셔너리에서 value값에 접근해서 sorted 함수의 정렬 키값으로 넘기기 위해 사용

test = {"banana": 3, "apple": -3, "carrot": 1}

# 방법1

test4 = sorted(test.items(), key=operator.itemgetter(1))
print(test4)

# 방법2

test5 = sorted(test.items(), key=lambda x: x[1])

#################value만 추출해 리스트로#################

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print(list(a.values()))
