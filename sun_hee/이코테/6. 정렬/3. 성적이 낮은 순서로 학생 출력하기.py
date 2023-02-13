# 성적이 낮은 순서대로 학생의 이름을 출력
n = int(input())
array = []
for i in range(n):
    array.append(input().split())


# print(array)
count = [0] * 101

for i in range(n):
    index = int(array[i][1])
    count[index] += 1

for i in range(len(count)):
    for j in range(count[i]):
        for a in array:
            if str(i) == a[1]:
                print(a[0], end=" ")
