n = int(input())
paper_list = []

for i in range(n):
    paper_list.append(int(input()))

# n = 3
# paper_list = [10, 20, 40]

paper_list.sort()
cmp = paper_list[0]+paper_list[1]

for i in range(2, n):
    cmp += (paper_list[i] + cmp)
print(cmp)
