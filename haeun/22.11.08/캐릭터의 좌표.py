def solution(keyinput, board):
    move = list(keyinput)
    row = (board[0]-1)//2
    col = (board[1]-1)//2
    answer = [0, 0]
    for i in move:
        if i == 'left':
            answer[0] -= 1
        elif i == 'right':
            answer[0] += 1
        elif i == 'up':
            answer[1] += 1
        else:
            answer[1] -= 1
    if abs(answer[0]) > row:
        if answer[0] >= 0:
            answer[0] = row
        else:
            answer[0] = -row
    if abs(answer[1]) > col:
        if answer[1] >= 0:
            answer[1] = col
        else:
            answer[1] = -col

    return answer
