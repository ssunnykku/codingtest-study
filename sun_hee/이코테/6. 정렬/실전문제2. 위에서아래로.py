n = int(input())
array = []
for i in range(n):
    x = int(input())
    array.append(x)


def sort_num(array):
    result = sorted(array, reverse=True)
    return " ".join(map(str, result))


print(sort_num(array))
