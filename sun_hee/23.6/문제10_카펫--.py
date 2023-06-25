# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 다시!!!!!!!!!!!!!!!

# yellow 1줄일 때
# 24*2+(1+2)*2
# [24+2,1+2]

# 2줄
# 24/2 => 12
# 12*2 +(2+2)*2
# [12+2, 2+2]

# 4줄 (yellow i줄)
# 24/4 => 6
# 6*2 + (4+2)*2
# [6+2,4+2]

brown = 12
yellow = 5


def solution(brown, yellow):
    answer = []

    # yellow가 홀수일 때
    if yellow % 2 != 0:
        return [yellow + 2, 3]

    # yellow를 몇 줄씩(h) 쌓아야 brown이 해당 개수가 될지 찾기
    for h in range(1, yellow // 2 + 1):
        # y: yellow의 가로
        y = yellow // h
        # y줄로 yellow를 쌓았을 때 필요한 brown의 개수
        b = (y * 2) + (h + 2) * 2
        #  b가 brown과 같으면
        print(y, b)
        if b == brown:
            # yellow의 가로 세로를 둘러야 되니까! yellow의 가로 세로에 2씩 더해줌
            answer.append(y + 2)
            answer.append(h + 2)
            break
    return answer


print(solution(brown, yellow))
