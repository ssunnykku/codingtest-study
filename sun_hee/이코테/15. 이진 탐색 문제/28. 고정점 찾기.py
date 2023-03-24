# 고정점 : 값이 인덱스와 동일
# 고정점을 출력, 없으면 -1

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid)
    else:
        return binary_search(array, mid, end)
    
n = int(input())
array = list(map(int, input().split()))

result = binary_search(array, array[0], array[n-1])
if result == None:
    print(-1) 
else:
    print(result)