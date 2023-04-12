# https://school.programmers.co.kr/learn/courses/30/lessons/172928

park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]

x,y = 0,0

for i in range(len(routes)):
    if routes[i][0] == 'E':
        y += int(routes[i][2])
    elif routes[i][0]  == "S":
        x += int(routes[i][2])
    elif routes[i][0] == "N" :
        y -= int(routes[i][2])
    else:
        x -= int(routes[i][2])

print(x,y)