# n명에 대하여 사용 시간표를 만든다.
# 사용하려는 시간, 끝나는 시간이 주어질 때 최대한 많은 사람이 회의실을 이용할 수 있도록 시간표를 만든다.
# 이용 시간의 시작 시간과 끝나는 시간이 같을 수도 있다. (ex> 3 3)
# 입력 : 이용자의 수 n과 순서대로 이용자의 시작시간과 끝나는 시간을 입력한다.
# 출력 : 이용할 수 있는 최대 인원 수를 출력한다.

# 풀이
# 끝나는 시간 기준으로 정렬
# 시작시간 순서로 확인하기. 겹치면 빼기

n = int(input())
cnt = 1
time = {}
for i in range(n):

    a, b = map(int, input().split())
    # 끝나는 시간을 key값으로 넣기
    time[b] = a
    # [(),()] 형태로 정렬됨
time = sorted(time.items())


for i in range(len(time)):
    if time[i][1] >= time[i+1][1]:
        cnt += 1

print(cnt)

# 위 코드는 틀린거임!! 문제점 : 시작 시간을 먼저 정렬하고 끝나는 시간을 정렬 해야됨!!
