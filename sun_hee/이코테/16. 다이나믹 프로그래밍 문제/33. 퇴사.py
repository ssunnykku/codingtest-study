# n : 남은 날짜
# t : 상담 기간
# p : 가격

# 먼저 할수 있는 일정부터 모으기

n = int(input())
array = [()]
for _ in range(n):
    array.append(tuple(map(int,input().split())))

# n = 7
# array = [[],[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]
result = []
new = []
for i in range(n):
    index = -(i+1)
    # -(i+1) 거꾸로 탐색
    # i+1 : 가능한 상담일 수
    if array[index][0] > i+1:
        continue
    # array[index] : 가능한 스케줄 역순으로 출력
    d = array.index(array[index])
    # array.index(array[index]) 인덱스 찾기, 날짜
    # 끝나는 날짜 : d+array[index][0]-1
    start = n+index+1 
    end = d+array[index][0]-1
    a = [a for a in array[index]]
    a.append(start) # 상담 시작일 추가
    a.append(end) # 끝나는 날짜 추가
    new.append(a)

# new : [[상담기간,가격,예약 시작, 예약 끝나는 날]]
array2 = sorted(new, key= lambda x:(x[3],x[2]))
# [[3, 10, 1, 3], [1, 10, 3, 3], [1, 20, 4, 4], [5, 20, 2, 6], [2, 15, 5, 6]]

for j in range(len(array2)):
    r = array2[j][1]
    a = array2[j][3]
    for i in range(j+1,len(array2)):
        if a < array2[i][2]:
            r += array2[i][1]
            a = array2[i][3]
    result.append(r)
print(max(result))

# 교재 풀이
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)