# N개의 통나무를 원형으로 세워 놓고 뛰어 놀기
# 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값
# 주어진 통나무로 만들 수 있는 가장 낮은 난이도의 배열을 출력하기

# 풀이 : 최댓값을 가운데 넣고, 그 다음 수를 양쪽으로?
# 난이도를 구하기 (인접한 수와의 차)

# # T = 테스트 케이스
T = int(input())
# # N = 통나무 개수
# # 통나무의 높이
for i in range(T):
    N = int(input())
    trees = sorted(list(map(int, input().split())), reverse=True)
    re_trees = []
    result = 0
    for i in range(N):
        if i % 2 == 0:
            re_trees.append(trees[i])
        else:
            re_trees.insert(0, trees[i])
    for i in range(N):
        if abs(re_trees[-i]-re_trees[-(i+1)]) > result:
            result = abs(re_trees[-i]-re_trees[-(i+1)])
    print(result)

# 메모리 116544KB
# 시간 296ms

# 다른사람 풀이 1
# 메모리 30220kb 시간 2220ms
n = int(input())

for i in range(n):
    m = int(input())
    arr = sorted(list(map(int, input().split())))
    max = 0
    for j in range(2, len(arr)):
        if arr[j]-arr[j-2] > max:
            max = arr[j] - arr[j-2]

    print(max)


# 다른사람 풀이2
# 가장 큰 통나무를 가운데에 두고 양옆을 그 다음으로 큰 통나무를 세우는 형식으로 반복하기

# T = int(input())

# for i in range(T):
#     N = int(input())
#     trees = list(map(int, input().split()))
#     trees.sort()
#     result = 0
#     for j in range(2, N):
#         result = max(result, abs(trees[j]-trees[j-2]))
#     print(result)
