# 사과품질 = 1점 ~ k점
# m개씩 포장
# 가격 : p(가장 낮은 품질 사과 점수) * m
# 최대 이익 계산

# 풀이
# 네개의 합이 가장 큰 조합 먼저 구해볼까?
# 정렬해서 큰 수 조합부터 포장
# 점수당 가격 구하기 점수: 가격(점수*m)

k = 4
m = 3

apples = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
apples.sort()
print(apples)

boxes = []
result = 0

while True:
    if len(apples) < m:
        break
    result += min(apples[-m:])*m
    print(apples[-m:])
    del apples[-m:]


print(result)
