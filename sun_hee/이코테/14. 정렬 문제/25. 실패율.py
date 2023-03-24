# 전체 스테이지의 개수 N
# 스테이지 배열 stages (현재 멈춰있는...), 마지막 스테이지 클리어 n+1
# 실패율 높은 스테이지부터 내림차순으로
# 실패율 = 스테이지 도달했으나 아직 클리어 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수

# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의
n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

result = []
length = len(stages)


for i in range(1, n+1):
    count = stages.count(i)
    length -= count
    fail = 0
    if count == 0:
        fail = 0
    else:
        fail = count / length
    result.append((i, fail))

answer = sorted(result, key=lambda x: x[1], reverse=True)
answer = [i[0] for i in answer]
print(answer)

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]


# def solution(N, stages):
#     answer = []
#     length = len(stages)

#     # 스테이지 번호를 1부터 N까지 증가시키기
#     for i in range(1, N + 1):
#         # 해당 스테이지에 머물러 있는 사람 수 계산
#         count = stages.count(i)

#         # 실패율 계산
#         if length == 0:
#             fail = 0
#         else:
#             fail = count / length

#         # 리스트에 (스테이지 번호, 실패율) 원소 삽입
#         answer.append((i, fail))
#         length -= count

#     # 실패율을 기준으로 각 스테이지를 내림차순 정렬
#     answer = sorted(answer, key=lambda t: t[1], reverse=True)

#     # 정렬된 스테이지 번호 출력
#     answer = [i[0] for i in answer]
#     return answer


# print(solution(N, stages))
