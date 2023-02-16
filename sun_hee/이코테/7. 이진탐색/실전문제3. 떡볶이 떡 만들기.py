import time


#  떡의 개수 n과 요청한 떡의 길이 m
n, m = map(int, input().split())
#  떡의 개별 높이
h = list(map(int, input().split()))

start_time = time.time()
# n, m = 4, 6
# h = [19, 15, 10, 17]


for i in range(max(h), 0, -1):
    result = 0
    for j in h:
        if (j - i) >= 0:
            result += (j - i)
        else:
            continue
    if result >= m:
        print(i)
        # print(result)
        break

end_time = time.time()
print("time: ", end_time-start_time)
