# [0, 0]
# up : [0, 1]
# down : [0, -1]
# left : [-1, 0]
# right: [1, 0]

# return [x, y]


# def solution(keyinput, board):
#     answer = []
#     return answer

# 일단 크기를 고려하지 않고 해보기

# keyinput = ["left", "right", "up", "right", "right"]
keyinput = ["down", "down", "down", "down", "down"]

# 1. 일단 고려 x
up = 0
down = 0
left = 0
right = 0
result = []
for i in (keyinput):
    if i == "left":
        left = left - 1
    if i == "right":
        right = right + 1
    if i == "up":
        up = up + 1
    if i == "down":
        down = down - 1
result.append(left+right)
result.append(up+down)

print(result)

# board 를 고려해봐
# board = [11, 11]
board = [7, 9]
# if result[0] > 0:
#     while result[0] > board[0]//2:
#         result[0] = result[0]-1
# elif result[0] < 0:
#     while abs(result[0]) > board[0]//2:
#         result[0] = result[0]+1

# if result[1] > 0:
#     while result[1] > board[1]//2:
#         result[1] = result[1]-1
# elif result[1] < 0:
#     while abs(result[1]) > board[1]//2:
#         result[1] = result[1]+1

# print(result)

# while문 없애 .. 더 많이 틀리네..?

if result[0] > 0 & result[0] > board[0]//2:
    result[0] = board[0]//2
elif result[0] < 0 & abs(result[0]) > board[0]//2:
    result[0] = -board[0]//2

if result[1] > 0 & result[1] > board[1]//2:
    result[1] = board[1]//2
elif result[1] < 0 & abs(result[1]) > board[1]//2:
    result[1] = -board[0]//2

print(result)
