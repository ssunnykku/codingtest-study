# 3이 하나라도 포함되는 모든 경우의 수
# N시 59분 59초

# 완전 탐색, 탐색해야 할 전체 데이터의 개수가 100만 개 이하일 때 사용

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
