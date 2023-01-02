
arr = [1, 1, 3, 3, 0, 1, 1]


answer = [arr[0]]
for i in range(1, len(arr)):
    answer.append(arr[i])
    if answer[len(answer)-1] == answer[len(answer)-2]:
        answer.pop()
