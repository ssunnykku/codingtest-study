# https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3
s =  "aukks"
skip =  "wbqd"
index = 5

array = 'abcdefghijklmnopqrstuwxyz'
# array = ['a','c','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','x','y','z']
# print(len(array))
for sk in skip:
    if sk in array:
        array.replace(sk,'')

result = []
for i in range(len(s)):
    array_index = array.index(s[i])+index
    if array_index >= len(array):
        result.append(array[array_index-len(array)-1])
    else:
        result.append(array[array_index])

print(result)