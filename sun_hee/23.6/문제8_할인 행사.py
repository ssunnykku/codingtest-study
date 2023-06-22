# https://school.programmers.co.kr/learn/courses/30/lessons/131127

# 10시까지
#  회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수
# 10일 간 회원자격
want = ["banana", "apple", "rice", "pork", "pot"]

number = [3, 2, 2, 2, 1]

discount = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]


def solution(want, number, discount):
    answer = 0
    # 할인 목록을 전체 순회
    for i in range(len(discount)):
        #  원하는 항목이 있으면 해당 항목부터 10개를 array에 담는다.
        if discount[i] in want:
            array = discount[i : i + 10]
            count_item = [0] * len(want)
            # array를 순회하며 원하는 아이템을 발견하면 count_item에 1을 더해준다.
            for j in range(len(array)):
                if array[j] in want:
                    index = want.index(array[j])
                    count_item[index] += 1
            #  count_item을 확인해 원하는 갯수보다 할인 아이템의 수가 많거나 같으면 result 해당 인덱스에 1을 넣어준다.
            result = [0] * len(want)
            for a in range(len(count_item)):
                if count_item[a] >= number[a]:
                    result[a] = 1
            # result의 요소가 1이면 구매 가능한 항목이므로 number 길이와 같으면 answer에 1을 더해준다.
            if sum(result) == len(number):
                answer += 1

    return answer


print(solution(want, number, discount))
