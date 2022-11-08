# 경우의 수 나열해보기

# n = 5  # 전체 학생 수
# lost = [2,4]  # 도난
# reserve = [1, 3, 5]  # 가져온 학생 번호
# return 5  # 들을 수 있는 학생

# 5명 - 2명 도난 + 3명 가져옴 - 중복1 = 5명

# n = 5
# lost = [2, 4]
# reserve = [3]
# return 4

# 5명 - 2명 도난 + 1명 가져옴 = 4

# n = 3
# lost = [3]
# reserve = [1]
# return = 2

# 3명 - 1명 도난 + 1명 가져옴 근데 조건에 안맞음 = 2


# 가져와는 데 도난 => 0으로 간주

# 전체 인원 - 2명 도난 + 1명 가져옴
# 조건 :  n 이 가져왔을 경우 n-1 , n+1만 입을 수 있음

def solution(n, lost, reserve):
    for i in reserve:
        for v in lost:
            # 빌려줄 수 있는거 찾기
            if i - 1 == v or i + 1 == v:
                return n - len(lost) + len(reserve)
            else:
                return n - len(lost)


print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [2, 4], [3]))

# n = 5  # 전체 학생 수
# lost = [2, 4]  # 도난
# reserve = [1, 3, 5]  # 가져온 학생 번호

# a = []
# for i in reserve:
#     for v in lost:
#         if i-1 == v or i + 1 == v:
#             a.append(i)
#             a.append(v)

# print(set(a))


# 체육복의 수만 세보기
# n = 5  # 전체 학생 수
# lost = [2, 4]  # 도난
# reserve = [1, 3, 5]  # 가져온 학생 번호

# count = n-len(lost)+len(reserve)
# if count > n:
#     count-(count-n)

# def solution(n, lost, reserve):
#     a = []
#     for i in reserve:
#         for v in lost:
#             if i - 1 == v or i + 1 == v:
#                 a.append(i)
#                 a.append(v)
#     result = set(a)
#     return result


# print(solution(5, [2, 4], [3]))
# print(solution(3, [3], [1]))
# print(solution(5, [2, 4], [3]))
