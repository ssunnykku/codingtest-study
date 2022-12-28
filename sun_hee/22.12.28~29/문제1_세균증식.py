# 세균 마리 수 n, 경과한 시간 t
# 1시간에 2배 증가
# 증가된 세균수를 구하기
n = 7
t = 15

# 2  = 2
# 2 * 2 = 4
# 4 * 2 = 8
# 8 * 2 = 16

# print(7) 0개
# print(7*2) 1개
# print(7*2*2) 2개
# print(7*2*2*2) 3개
# print(56*2)
# print(112*2)

list = []
for i in range(t+1):
    list.append(n*pow(2, i))
print(list[-1])


def solution(n, t):
    answer = 0
    return answer
