# 민우가 구매한 로또 번호를 담은 배열 lottos(길이 6인 정수 배열), 당첨 번호를 담은 배열 win_nums(길이 6인 정수 배열)

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(sorted(lottos, reverse=True))
print(sorted(win_nums, reverse=True))

correct_num = 0
count_zero = 0
for s_num in lottos:
    if s_num == 0:
        count_zero += 1
    for check in win_nums:
        if s_num == check:
            correct_num += 1
print(correct_num)
# print(count_zero)

rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

print(rank[correct_num])
# print(rank[correct_num+count_zero])
