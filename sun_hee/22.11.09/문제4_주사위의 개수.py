# 매개변수 : 가로,세로,높이, 모서리의 길이 n ex: [1,1,1]
# 결과 : 들어갈 수 있는 주사위 최대 갯수

# box = [10, 6, 8]
# n = 3

# box = [5, 5, 5]
# n = 5


# def solution(box, n):
#     if box == [1, 1, 1]:
#         w = math.ceil(box[0]/n)
#         v = math.ceil(box[1]/n)
#         h = math.ceil(box[2]/n)
#     else:
#         w = int(box[0]/n)
#         v = int(box[1]/n)
#         h = int(box[2]/n)

#     return w * v * h

def solution(box, n):
    if box[0] == n and box[1] == n and box[2] == n:
        return 1
    elif box[0] > n and box[1] > n and box[2] > n:
        w = int(box[0]/n)
        v = int(box[1]/n)
        h = int(box[2]/n)
    else:
        return 0

    return w * v * h
