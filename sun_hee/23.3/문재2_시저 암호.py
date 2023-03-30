# s : 문자열
# n : 거리
s = "abz"
s2 = s.lower()
n = 4

array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']

# 1. s[0]의 값(인덱스) 찾기
# 2. s[0]의 인덱스값에서 n의 값 더하기
# 3. 2에서 s의 길이만큼 인덱스를 더해 출력하기
target = s2[0]
start = 0
end = 24
def binary_search(array, start, end, target):
    if start > end:
        return None
    
    mid = (start+end) // 2

    if array[mid] == target:
        if mid > 24:
            return mid-24
        return mid
    
    elif array[mid] > target:
        # print(array[mid] > target)
        return binary_search(array, start, mid - 1, target)
    else:
        return binary_search(array, mid + 1, end, target)
    
index = binary_search(array, start, end, target)
if index >= 0:
    print(''.join(array[index+n:len(s)+n]))
else:
    print(''.join(array[index-n:-len(s)-n]))