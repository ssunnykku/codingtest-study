dots = [[1, 4], [1, 4], [3, 8], [3, 8]]

arr = []
test = []
for i in range(len(dots)):
    for j in range(-len(dots)+i+1, 0):
        print(dots[i], dots[j], j)
        test.append([abs(dots[i][0]-dots[j][0]), abs(dots[i][1]-dots[j][1])])

result = 0
for x in range(len(test)):
    for y in range(-len(test)+x+1, 0):
        if test[x] == test[y]:
            result += 1

if result != 0:
    print(1)
print(test)
