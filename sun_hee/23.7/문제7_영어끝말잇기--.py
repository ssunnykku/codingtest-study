# https://school.programmers.co.kr/learn/courses/30/lessons/12981

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# 탈락자 기준 : 끝말잇기 틀렸을 때
# 나온 단어 말했을 때
# 출력할 것 : 몇번째 사람인지, 몇번째 말했는지

# 몇 번째 사람인지는 인덱스 % n + 1
# 몇 번째 게임인지는 인덱스 // n + 1

def solution(n, words):
   p = [words[0][0]]
   for i, w in enumerate(words):
      if w not in p and p[-1][-1] == w[0]:
         print(i,w)
         p.append(w)
      else:
         return [i % n + 1, (i//n)+1]
   return [0,0]

print(solution(n,words))