# 11시 30분까지
# 풀이 : numbers를 반복문 돌려서 모든 연산 해보기
# target과 값이 같으면 횟수 세주기
# 모르겠어.. BFS 공부하고 올게~

# numbers = [1, 1, 1, 1, 1]
numbers = [4, 1, 2, 1]
# target = 3
target = 4

for number in numbers:
    print(sum(numbers)-number)
