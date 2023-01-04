numbers = [1, 2, 3, 4, 6, 7, 8, 0]
standard = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = []

for i in numbers:
    if i in standard:
        standard.remove(i)
print(sum(standard))
