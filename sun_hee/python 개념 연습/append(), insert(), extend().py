a = [1, 2, 3]
a.append(4)
a
# [1, 2, 3, 4]

# array.insert(i, x) 형태

nums = [1, 2, 3]
nums.insert(0, [10, 20])  # 0번째(맨앞에) 추가
# [[10, 20], 1, 2, 3]

nums.insert(-1, 100)  # 끝에서 1번째 전에 추가
print(nums)
# [[10, 20], 1, 2, 100, 3]  # 리스트 맨 끝에 저장되지 않음

# array.extend(iterable) 형태로 사용
# 입력한 iterable 자료형의 항목 각각을 array의 끝에 하나씩 추가한다. append와 동일하게 요소를 array의 끝에 추가하지만 append와 다른 점은 괄호( ) 안에는 iterable 자료형만 올 수 있다는 것이다. iterable 자료형이 아닌 경우 TypeError가 발생한다.

nums = [1, 2, 3]
nums.extend([4, 5])
# [1, 2, 3, 4, 5]  # 리스트로 주어진 [4, 5]의 요소가 각각 추가 되었음

a = [10]
nums.extend(a)
# [1, 2, 3, 4, 5, 10]
