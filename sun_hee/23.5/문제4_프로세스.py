# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 실패...
citations = [5, 4, 3, 2, 1]

# cnt = 0
citations.sort(reverse=True)

for i in citations:
    h = citations.index(i) + 1
    if i >= h:
        print(h)
        print(len(citations) - h - 1)
# print(cnt)
