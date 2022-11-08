# 고민 과정

# A[0] = h 일 때 B[n] = h , n 찾기
# B[n],B[n+1] ... 로 배열 해보기
# B[n+1] 과 A[1]이 같은지 확인


# 처음 시도

# def solution(A, B):
#     find_index = B.index(A[0])

#     x = []
#     for i in range(find_index, len(A)):
#         x.append(B[i])

#     y = "".join(x)
#     if y == A[:len(A)-find_index]:
#         return len(A)-len(x)
#     else:
#         return -1


# 두번 째 시도

A = "hello"
B = "ohell"
find_index = B.index(A[0])

# print(B[find_index], B[find_index+1], B[find_index+2],
#       B[find_index+3], B[find_index+4-5])

x = []
for i in range(find_index, len(A)):
    x.append(B[i])

for v in range(find_index-1, 1):
    x.append(B[v])

y = str("".join(x))
if y == A:
    print(len(A)-(len(A)-find_index))
else:
    print(-1)

# 실패 원인 ? hhhhhello 처럼 중복되어서 문자가 나타날 수 있음
