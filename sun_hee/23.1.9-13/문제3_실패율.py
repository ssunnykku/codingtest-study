# 10시 5분 ~ 10시 30분

# 실패율 = 스테이지 도달 O, 클리어 실패 플레이어 수 / 스테이지 도달 O
# 전체 스테이지의 개수 N, 게임 사용자가 현재 멈춰있는 스테이지 배열 stages, 실패율 높은 스테이지부터 내림차순으로 스테이지 번호의 배열을 return

# 풀이
# N으로 반복문을 돌려 각 스테이지별 실패율을 구해 딕셔너리에 담기 {스테이지:실패율}
# 실패율(딕셔너리의 value)을 기준으로 내림차순 정렬
# 스테이지(key)를 리스트에 담기

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 500
# stages = [1]*200000
failure_rate = {}
cnt = 0
failure = 0

for i in range(N):
    for level in stages:
        if level >= i+1:
            cnt += 1
    failure = stages.count(i+1)
    if cnt == failure == 0:
        failure_rate[i+1] = 0
    else:
        failure_rate[i+1] = failure/cnt
        cnt = 0
        failure = 0

result = dict(sorted(failure_rate.items(), key=lambda x: x[1], reverse=True))

print(list(result.keys()))
