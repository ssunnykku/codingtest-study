# https://school.programmers.co.kr/learn/courses/30/lessons/87390

n = 4
left = 7
right = 14

# 1 2 3
# 2 2 3 
# 3 3 3

#  시간초과
# def solution(n, left, right):
    # 수를 1부터 n개까지 순서대로 n번 나열해 리스트에 담음
#     answer = list(range(1,n+1))*n
#     answer.sort()

#     for i in range(n):
#         for j in range(i,right+1,n):
            # answer[j]가 answer[i](첫줄, 기준) 보다 작으면 기준으로 바꿔줌
#             if answer[j] < answer[i]:
#                 answer[j] = i+1
    
#     return answer[left:right+1]


def solution(n, left, right):
    standard = list(range(1,n+1))
    answer = []
    # 기준인덱스 구하기 (첫 줄)
    for i in range(left,right+1):
        index = i%n
        line = i//n+1
        if standard[index] > line:
            answer.append(standard[index])
        else:
            answer.append(line)

    return answer
print(solution(n,left,right))

# 다른사람 코드
# def solution(n, left, right):
#     answer = []
#     for i in range(left,right+1):
#         answer.append(max(i//n,i%n)+1)
#     return answer