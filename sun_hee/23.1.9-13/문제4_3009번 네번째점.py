# 세 점이 주어졌을 때 축에 평행한 직사각형을 만들기 위해서 필요한 네 점을 찾는 프로그램을 완성하시오.
# 유형 : 구현

# 풀이
# 주어진 수에서 x좌표와 y좌표가 두 개씩 값이 같을 때 축에 평행한 직사각형이 된다.
# x축끼리, y축끼리 리스트에 담은 후
# 해당 숫자가 하나만 있는 경우 그 값을 변수에 담아 출력한다.

x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()

X = [x1, x2, x3]
Y = [y1, y2, y3]


for i in X:
    if X.count(i) == 1:
        ans_x = int(i)
        break
for i in Y:
    if Y.count(i) == 1:
        ans_y = int(i)
        break
print(ans_x, ans_y)
