n = int(input())
moving = input().split()

location = [1,1]

for i in moving:
    if i == 'R' and location[1] != 5:
        location[1] += 1
    elif i == 'L' and location[1] != 1:
        location[1] -= 1
    elif i == 'U' and location[0] != 1:
        location[0] -= 1
    elif i == 'D' and location[0] != 5:
        location[0] += 1

print(location)