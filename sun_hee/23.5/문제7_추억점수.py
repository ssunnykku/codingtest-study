# 1시까지
name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]


def solution(name, yearning, photo):
    answer = []
    for j in photo:
        point = 0
        for i in range(len(name)):
            if name[i] in j:
                point += j.count(name[i]) * yearning[i]
        answer.append(point)

    return answer


print(solution(name, yearning, photo))
