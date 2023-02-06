# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# N * M 형태 , N : 행의 개수, M : 열의 개수
# 뽑고자 하는 카드가 포함되어 있는 행을 선택, 선택된 카드들 중 가장 숫자가 낮은 카드를 뽑기
# 뽑힌 숫자들 중 가장 높은 숫자의 카드를 출력
# 첫째 줄 N M : 행의 개수 열의 개수

# 풀이
# 모든 행에서 가장 작은 수를 추출
# 크기를 비교 하여 가장 큰 수가 남게 하기

n, m = map(int, input().split())
result = []

for i in range(n):
    min_value = min(list(map(int, input().split())))
    result.append(min_value)

print(max(result))

# 교재 답안
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 교재 답안 2 2중 반복문 구조 이용해서 직접 해보기. p100
