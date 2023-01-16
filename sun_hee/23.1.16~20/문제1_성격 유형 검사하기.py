# 7시 20분 ~ 50분!!
# 카카오 성격 유형 검사지 만들기

# 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 맏은 성격 유형이 검사자의 성격 유형

# 같으면 둘 중에 사전 순으로

# survey[i]의 첫번째 캐릭터 : i+1번 질문의 비동의 관련 선택지 선택
# survey[i]의 첫번째 캐릭터 : i+1번 질문의 동의 관련 선택지 선택

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
# result = "TCMA"
# A : 비동의 : 1~3
# N : 동의 : 5~7
# len(choices) : 서베이 길이

# 풀이 :
# survey, choices 이중 반복문, choices가 1~3인 경우 survey 요소의 [0] 출력

answer = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

for i in range(len(survey)):
    if choices[i] == 1:
        answer[survey[i][0]] += 3
    elif choices[i] == 2:
        answer[survey[i][0]] += 2
        # print(survey[i][0], "2점")
    elif choices[i] == 3:
        answer[survey[i][0]] += 1
        # print(survey[i][0], "1점")
    elif choices[i] == 5:
        answer[survey[i][1]] += 1
        # print(survey[i][1], "1점")
    elif choices[i] == 6:
        answer[survey[i][1]] += 2
        # print(survey[i][1], "2점")
    elif choices[i] == 7:
        # print(survey[i][1], "3점")
        answer[survey[i][1]] += 3
print(answer)
result = list(answer.values())

# 모르게쒀~~
