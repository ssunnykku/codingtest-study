# https://wikidocs.net/22804

# lambda: 익명함수
# 장점: 코드의 간결함, 메모리의 절약
# 재사용할 필요 없을때. 물론 람다함수도 객체이므로 재사용이 필요하다면 정의와 동시에 변수에 담으면 됨
# def test(x):
#     return x+1
# 1
test = (lambda x: x + 1)(3)
print(test)

# 2


def func(x): return x + 1


print(func(4))

# 3
# 앞 뒤 불필요한 공백을 제외한 문자의 길이로 정렬하기
# sorted함수의 경우 key위치인자에 함수를 보내서, 함수에서 지장한 결과값에 따라서 정렬을 할 수 있습니다.
# string.strip():공백제거
target = ['  cat ', ' tiger ', '    dog', 'snake   ']


def my_key(string):
    return len(string.strip())


# 안되는데..?
# print(sorted(target, key=lambda x: len(x.strip())))
