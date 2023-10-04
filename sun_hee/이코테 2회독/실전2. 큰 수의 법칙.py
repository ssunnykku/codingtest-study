# n = 5
# m = 8
# k = 3
# array = [2,4,5,4,6]

def solution():
    n,m,k = map(int, input().split())
    array = list(map(int, input.split()))

    array.sort(reverse=True)
    arr = [array[0],array[0],array[0],array[1]]
    while(True):
        arr= arr + arr
        if len(arr) > m:
            break

    return sum(arr[:m])

print(solution())