s = "AB"
n = 1

def solution(s, n):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','w','x','y','z']
    input = s.lower()
    result =alphabet[alphabet.index(input[0])+1:len(s)+1]

    answer = ''.join(result)
    return answer

print(solution(s,n))