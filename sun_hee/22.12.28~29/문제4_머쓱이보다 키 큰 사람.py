array = [149, 180, 192, 170]
height = 167
result = 3

cnt = 0
for h in array:
    if h > height:
        cnt += 1

print(cnt)

def solution(array, height):
    cnt = 0
    for h in array:
        if h > height:
            cnt += 1

    return cnt

