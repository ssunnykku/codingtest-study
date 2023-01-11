test = ["R", "R", "R", "U", "D", "D"]
test_int = [1, 2, 3, 4, 5]

# 1. 값 input으로 리스트로 입력받기
# 1-1. str
# str_list = list(map(str, input().split()))

# 1-2. int
# int_list = list(map(int, input().split()))

# 2. 리스트 한번에 값만 출력하기 (ex) 1 2 3 4 5
print(" ".join(list(map(str, test_int))))
print(*test_int)
