# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 11시 20분까지 풀기

# 같은 종류 끼리 나열한 리스트 만들기!
# 각 리스트들의 길이를 구하기
# 길이의 합이 k가 되는 리스트 찾기
# 특정 리스트의 길이가 k보다 작다면, 가장 큰 길이 먼저 포함되도록 한다.

# 실패함~~
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
# [1, 2, 2, 3, 3, 4, 5, 5]
# 같은 종류 끼리 나열한 리스트 만들기!
# 각 리스트들의 길이를 구하기
tangerine.sort()
index_array = []
# 한 종류에 몇개 있는지 kind에 넣어주기
kind = []
for i in range(len(tangerine) - 1):
    if tangerine[i] != tangerine[i + 1]:
        if index_array == []:
            kind.append(i + 1)
        else:
            kind.append(i + 1 - index_array[-1])
        index_array.append(i + 1)

if sum(index_array) != len(tangerine):
    kind.append(len(tangerine) - index_array[-1])

kind.sort(reverse=True)
print(kind)

# 합이 k가 되는 조합 찾기
package = []
for i in kind:
    if sum(package) > k:
        package.pop()
    elif sum(package) < k:
        package.append(i)
    elif sum(package) == k:
        break
answer = len(package)
print(answer)
