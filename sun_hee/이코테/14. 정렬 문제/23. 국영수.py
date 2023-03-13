# # n = int(input())
# # 학생이름, 국어, 영어, 수학
# # 국어 점수가 감소하는 순서로
# # 국어 점수가 같으면 영어 점수 증가하는 순서
# # 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

# # students = []
# # for i in range(n):
# #     name, k, e, m = input().split()
# #     students.append([str(name), int(k), int(e), int(m)])

# students = [["Junkyu", 50, 60, 100], ["Sangkeun", 80, 60, 100]]
# # print(students)
# sort_result = sorted(students, key=lambda x: (-x[1], +x[2], +x[0]))

# for x in sort_result:
#     print(x[0])

# 다시

n = int(input())

students = []
for _ in range(n):
    students.append(input().split())

# students = [("Junkyu", 50, 60, 100), ("Sangkeun", 80, 60, 100)]
# print(students)
students.sort(key=lambda x: (-int(x[1]), +int(x[2]), -int(x[3]), x[0]))
# print(students)
for x in students:
    print(x[0])
